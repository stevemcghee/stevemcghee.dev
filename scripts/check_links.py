import re
import requests
import os
from concurrent.futures import ThreadPoolExecutor

def extract_links(directory):
    external_links = set()
    internal_links = set()
    # Pattern for external URLs
    ext_pattern = re.compile(r'https?://[a-zA-Z0-9./?=_%&+-]+')
    # Pattern for internal links like /images/foo.jpg or /resume.pdf
    int_pattern = re.compile(r'(?<=["\'\(])(/[a-zA-Z0-9./_-]+\.[a-zA-Z0-9]+)(?=["\'\)])')
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.md', '.yml', '.yaml', '.html', '.css')):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # External
                        ext_matches = ext_pattern.findall(content)
                        for url in ext_matches:
                            url = url.rstrip(').,">\'')
                            external_links.add((url, path))
                        # Internal
                        int_matches = int_pattern.findall(content)
                        for link in int_matches:
                            internal_links.add((link, path))
                except Exception as e:
                    print(f"Error reading {path}: {e}")
    return external_links, internal_links

def check_external(url_data):
    url, path = url_data
    if "UNKNOWN" in url or "example.com" in url:
        return f"PLACEHOLDER: {url} in {path}"
    try:
        # User-Agent to avoid some bot detection
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        response = requests.head(url, timeout=10, allow_redirects=True, headers=headers)
        if response.status_code >= 400:
            response = requests.get(url, timeout=10, allow_redirects=True, headers=headers)
            if response.status_code >= 400:
                return f"BROKEN EXT ({response.status_code}): {url} in {path}"
    except Exception as e:
        return f"FAILED EXT: {url} in {path} ({e})"
    return None

def check_internal(link_data):
    link, path = link_data
    # Convert absolute-style path to relative file path
    # assuming links starting with / refer to static/ or content/ (after Hugo build)
    # For now, we check if they exist in static/ or as a .md in content/
    clean_link = link.lstrip('/')
    possible_paths = [
        os.path.join('static', clean_link),
        os.path.join('content', clean_link),
        os.path.join('content', clean_link.replace('.html', '.md'))
    ]
    
    if any(os.path.exists(p) for p in possible_paths):
        return None
    
    # Special case for directories (About -> /about/)
    if os.path.isdir(os.path.join('content', clean_link)):
        return None

    return f"BROKEN INT: {link} in {path}"

def main():
    print("Extracting links...")
    ext_content, int_content = extract_links('content')
    ext_data, int_data = extract_links('data')
    ext_assets, int_assets = extract_links('assets')
    ext_layouts, int_layouts = extract_links('layouts')
    
    all_ext = ext_content.union(ext_data).union(ext_assets).union(ext_layouts)
    all_int = int_content.union(int_data).union(int_assets).union(int_layouts)
    
    print(f"Found {len(all_ext)} external and {len(all_int)} internal link-file pairs.")
    
    print("Checking internal links...")
    broken_int = [check_internal(l) for l in all_int]
    
    print("Checking external links...")
    with ThreadPoolExecutor(max_workers=10) as executor:
        results_ext = list(executor.map(check_external, all_ext))
    
    broken = [r for r in broken_int + results_ext if r]
    if broken:
        print("\nBroken or Placeholder Links Found:")
        for b in sorted(broken):
            print(b)
    else:
        print("\nNo broken links found!")

if __name__ == "__main__":
    main()
