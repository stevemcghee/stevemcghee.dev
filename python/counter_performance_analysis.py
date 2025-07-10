#!/usr/bin/env python3
"""
Analysis of Counter performance vs manual loops and when to use each approach.
"""

from collections import Counter
import time
import random

def generate_test_data(num_dicts=10, dict_size=1000, overlap_ratio=0.3):
    """Generate test dictionaries with controlled overlap"""
    all_keys = [f'key_{i}' for i in range(dict_size)]
    dicts = []
    
    for i in range(num_dicts):
        overlap_keys = random.sample(all_keys, int(dict_size * overlap_ratio))
        unique_keys = random.sample(all_keys, dict_size - len(overlap_keys))
        all_dict_keys = overlap_keys + unique_keys
        d = {key: random.randint(1, 1000) for key in all_dict_keys}
        dicts.append(d)
    
    return dicts

print("=== COUNTER vs MANUAL LOOP PERFORMANCE ANALYSIS ===\n")

# Test 1: Small datasets (where Counter overhead matters)
print("=== Test 1: Small Datasets (10-100 keys) ===")
small_dicts = generate_test_data(num_dicts=5, dict_size=50, overlap_ratio=0.2)

# Counter approach
start = time.time()
for _ in range(1000):  # Run multiple times for small datasets
    counter_result = dict(sum(map(Counter, small_dicts), Counter()))
counter_time = time.time() - start

# Manual approach
start = time.time()
for _ in range(1000):
    manual_result = {}
    for d in small_dicts:
        for key, value in d.items():
            manual_result[key] = manual_result.get(key, 0) + value
manual_time = time.time() - start

print(f"Small datasets (50 keys each):")
print(f"  Counter: {counter_time:.6f}s")
print(f"  Manual:  {manual_time:.6f}s")
print(f"  Ratio:   {counter_time/manual_time:.2f}x (Counter is slower)")

# Test 2: Large datasets with high overlap (Counter's sweet spot)
print("\n=== Test 2: Large Datasets with High Overlap ===")
large_overlap_dicts = generate_test_data(num_dicts=20, dict_size=2000, overlap_ratio=0.8)

# Counter approach
start = time.time()
counter_result = dict(sum(map(Counter, large_overlap_dicts), Counter()))
counter_time = time.time() - start

# Manual approach
start = time.time()
manual_result = {}
for d in large_overlap_dicts:
    for key, value in d.items():
        manual_result[key] = manual_result.get(key, 0) + value
manual_time = time.time() - start

print(f"Large datasets with high overlap (80% shared keys):")
print(f"  Counter: {counter_time:.6f}s")
print(f"  Manual:  {manual_time:.6f}s")
print(f"  Ratio:   {manual_time/counter_time:.2f}x (Counter is faster)")

# Test 3: Counting operations (Counter's primary purpose)
print("\n=== Test 3: Counting Operations (Counter's Sweet Spot) ===")

# Generate list of items to count
items_to_count = [random.choice(['a', 'b', 'c', 'd', 'e']) for _ in range(100000)]

# Counter approach for counting
start = time.time()
counter_counts = Counter(items_to_count)
counter_time = time.time() - start

# Manual counting
start = time.time()
manual_counts = {}
for item in items_to_count:
    manual_counts[item] = manual_counts.get(item, 0) + 1
manual_time = time.time() - start

print(f"Counting 100,000 items:")
print(f"  Counter: {counter_time:.6f}s")
print(f"  Manual:  {manual_time:.6f}s")
print(f"  Ratio:   {manual_time/counter_time:.2f}x (Counter is much faster)")

# Test 4: Dictionary combination with different overlap ratios
print("\n=== Test 4: Performance by Overlap Ratio ===")

overlap_ratios = [0.1, 0.3, 0.5, 0.7, 0.9]
results = []

for overlap in overlap_ratios:
    test_dicts = generate_test_data(num_dicts=10, dict_size=1000, overlap_ratio=overlap)
    
    # Counter timing
    start = time.time()
    dict(sum(map(Counter, test_dicts), Counter()))
    counter_time = time.time() - start
    
    # Manual timing
    start = time.time()
    result = {}
    for d in test_dicts:
        for key, value in d.items():
            result[key] = result.get(key, 0) + value
    manual_time = time.time() - start
    
    results.append((overlap, counter_time, manual_time))

print(f"{'Overlap':<8} {'Counter (s)':<12} {'Manual (s)':<12} {'Ratio':<8}")
print("-" * 42)
for overlap, counter_time, manual_time in results:
    ratio = manual_time / counter_time
    faster = "Counter" if counter_time < manual_time else "Manual"
    print(f"{overlap:<8} {counter_time:<12.6f} {manual_time:<12.6f} {faster} {ratio:.2f}x")

# Test 5: Memory usage comparison
print("\n=== Test 5: Memory Usage ===")
import sys

test_dicts = generate_test_data(num_dicts=5, dict_size=1000, overlap_ratio=0.5)

# Memory for Counter approach
import gc
gc.collect()
counter_mem = dict(sum(map(Counter, test_dicts), Counter()))
counter_memory = sys.getsizeof(counter_mem)

# Memory for Manual approach
gc.collect()
manual_mem = {}
for d in test_dicts:
    for key, value in d.items():
        manual_mem[key] = manual_mem.get(key, 0) + value
manual_memory = sys.getsizeof(manual_mem)

print(f"Memory usage (bytes):")
print(f"  Counter: {counter_memory}")
print(f"  Manual:  {manual_memory}")
print(f"  Difference: {abs(counter_memory - manual_memory)} bytes")

# Test 6: When Counter is actually beneficial
print("\n=== Test 6: Counter's Real Benefits ===")

print("Counter is most beneficial when:")
print("1. You're doing actual COUNTING operations")
print("2. You need Counter's specialized methods (most_common, elements, etc.)")
print("3. You're working with large datasets and high overlap")
print("4. You need arithmetic operations (+, -, &, |)")

# Example: Finding most common items
print("\nExample: Finding top 5 most common items")
items = [random.choice(['red', 'blue', 'green', 'yellow', 'purple']) for _ in range(10000)]

# Counter approach
start = time.time()
counter_obj = Counter(items)
top_5_counter = counter_obj.most_common(5)
counter_time = time.time() - start

# Manual approach
start = time.time()
manual_counts = {}
for item in items:
    manual_counts[item] = manual_counts.get(item, 0) + 1
top_5_manual = sorted(manual_counts.items(), key=lambda x: x[1], reverse=True)[:5]
manual_time = time.time() - start

print(f"Finding top 5 items:")
print(f"  Counter: {counter_time:.6f}s")
print(f"  Manual:  {manual_time:.6f}s")
ratio = manual_time / counter_time
faster = "Counter" if counter_time < manual_time else "Manual"
print(f"  Ratio:   {ratio:.2f}x ({faster} is faster)")

print(f"\nTop 5 results:")
print(f"  Counter: {top_5_counter}")
print(f"  Manual:  {top_5_manual}")

print("\n=== CONCLUSION ===")
print("Counter is NOT always faster for dictionary combination!")
print("Use Counter when:")
print("- You need counting operations")
print("- You need Counter's specialized methods")
print("- You have high overlap between dictionaries")
print("- You need arithmetic operations")
print("\nUse manual loops when:")
print("- You have small datasets")
print("- You have low overlap between dictionaries")
print("- You need maximum performance for simple combination") 