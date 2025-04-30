import yaml
import os
from datetime import datetime

# Read the podcasts YAML file
with open('data/podcasts.yml', 'r') as file:
    podcasts = yaml.safe_load(file)

# Create podcasts directory if it doesn't exist
os.makedirs('content/podcasts', exist_ok=True)

# Generate markdown files for each podcast
for podcast in podcasts:
    # Create a slug from the title
    slug = podcast['title'].lower().replace(' ', '-').replace(':', '').replace('?', '')
    
    # Format the date
    date = datetime.strptime(podcast['date'], '%Y-%m-%d')
    formatted_date = date.strftime('%Y-%m-%d')
    
    # Create the markdown content
    content = f"""---
title: "{podcast['title']}"
date: {formatted_date}
description: "{podcast['description']}"
show: "{podcast['show']}"
podcast_url: "{podcast['link']}"
---

{podcast['description']}

Listen to this episode on [{podcast['show']}]({podcast['link']}).
"""
    
    # Write the file
    with open(f'content/podcasts/{slug}.md', 'w') as file:
        file.write(content)

print("Generated podcast entries successfully!") 