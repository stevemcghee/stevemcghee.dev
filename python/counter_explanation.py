#!/usr/bin/env python3
"""
Comprehensive explanation of Python's Counter class from collections module.
"""

from collections import Counter

print("=== COUNTER EXPLANATION ===\n")

# What is Counter?
print("Counter is a dict subclass for counting hashable objects.")
print("It's a container that keeps track of how many times equivalent values are added.\n")

# Basic Counter creation
print("=== 1. Basic Counter Creation ===")

# From iterable (most common)
letters = Counter('hello world')
print(f"Counter('hello world'): {letters}")

# From list
numbers = Counter([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
print(f"Counter([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]): {numbers}")

# From dictionary
word_counts = Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(f"Counter({{'apple': 3, 'banana': 2, 'cherry': 1}}): {word_counts}")

# From keyword arguments
colors = Counter(red=5, blue=3, green=2)
print(f"Counter(red=5, blue=3, green=2): {colors}")

print("\n=== 2. Counter Operations ===")

# Accessing counts
print(f"letters['l']: {letters['l']}")  # Count of 'l'
print(f"letters['z']: {letters['z']}")  # Returns 0 for missing items (not KeyError)

# Most common elements
print(f"letters.most_common(3): {letters.most_common(3)}")
print(f"numbers.most_common(): {numbers.most_common()}")

# Total count
print(f"letters.total(): {letters.total()}")  # Python 3.10+
print(f"sum(letters.values()): {sum(letters.values())}")

print("\n=== 3. Counter Arithmetic ===")

# Addition
c1 = Counter(['a', 'b', 'c', 'a', 'b'])
c2 = Counter(['a', 'b', 'd', 'd'])
print(f"c1: {c1}")
print(f"c2: {c2}")
print(f"c1 + c2: {c1 + c2}")  # Adds counts

# Subtraction
print(f"c1 - c2: {c1 - c2}")  # Subtracts counts (minimum 0)

# Intersection (minimum of counts)
print(f"c1 & c2: {c1 & c2}")

# Union (maximum of counts)
print(f"c1 | c2: {c1 | c2}")

print("\n=== 4. Counter Methods ===")

# elements() - returns iterator of elements
print("letters.elements():", list(letters.elements()))

# update() - adds counts
c3 = Counter(['x', 'y'])
print(f"Before update: {c3}")
c3.update(['x', 'x', 'z'])
print(f"After update: {c3}")

# subtract() - subtracts counts
c4 = Counter(['a', 'b', 'c', 'a'])
print(f"Before subtract: {c4}")
c4.subtract(['a', 'b'])
print(f"After subtract: {c4}")

print("\n=== 5. Counter for Dictionary Combination ===")

# This is why Counter is perfect for combining dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}
dict3 = {'a': 7, 'c': 8, 'e': 9}

print("Original dictionaries:")
print(f"dict1: {dict1}")
print(f"dict2: {dict2}")
print(f"dict3: {dict3}")

# Convert to Counters
counter1 = Counter(dict1)
counter2 = Counter(dict2)
counter3 = Counter(dict3)

print(f"\nAs Counters:")
print(f"counter1: {counter1}")
print(f"counter2: {counter2}")
print(f"counter3: {counter3}")

# Add them together
combined_counter = counter1 + counter2 + counter3
print(f"\nCombined: {combined_counter}")

# Convert back to dict
result_dict = dict(combined_counter)
print(f"As dict: {result_dict}")

print("\n=== 6. Why Counter is Perfect for This ===")

print("Counter automatically:")
print("- Handles missing keys (returns 0 instead of KeyError)")
print("- Adds values for duplicate keys")
print("- Provides efficient arithmetic operations")
print("- Can be converted back to regular dict")

print("\n=== 7. Alternative Without Counter ===")

# Manual approach
manual_result = {}
for d in [dict1, dict2, dict3]:
    for key, value in d.items():
        manual_result[key] = manual_result.get(key, 0) + value

print(f"Manual result: {manual_result}")
print(f"Counter result: {result_dict}")
print(f"Same result: {manual_result == result_dict}")

print("\n=== 8. Performance Comparison with Large Datasets ===")

import time
import random

# Generate large datasets with realistic data
def generate_large_dicts(num_dicts=10, dict_size=1000, overlap_ratio=0.3):
    """Generate multiple large dictionaries with controlled overlap"""
    all_keys = [f'key_{i}' for i in range(dict_size)]
    dicts = []
    
    for i in range(num_dicts):
        # Create some overlap between dictionaries
        overlap_keys = random.sample(all_keys, int(dict_size * overlap_ratio))
        unique_keys = random.sample(all_keys, dict_size - len(overlap_keys))
        all_dict_keys = overlap_keys + unique_keys
        
        # Create dictionary with random values
        d = {key: random.randint(1, 1000) for key in all_dict_keys}
        dicts.append(d)
    
    return dicts

print("Generating large datasets...")
large_dicts = generate_large_dicts(num_dicts=10, dict_size=1000, overlap_ratio=0.3)

print(f"Generated {len(large_dicts)} dictionaries with ~{len(large_dicts[0])} keys each")
print(f"Total unique keys across all dicts: {len(set().union(*[d.keys() for d in large_dicts]))}")

# Test different approaches
approaches = {}

# 1. Counter approach (our golf solution)
print("\n--- Testing Counter approach ---")
start = time.time()
counter_result = dict(sum(map(Counter, large_dicts), Counter()))
counter_time = time.time() - start
approaches['Counter'] = counter_time
print(f"Counter time: {counter_time:.6f} seconds")
print(f"Result size: {len(counter_result)} keys")

# 2. Manual loop approach
print("\n--- Testing Manual loop approach ---")
start = time.time()
manual_result = {}
for d in large_dicts:
    for key, value in d.items():
        manual_result[key] = manual_result.get(key, 0) + value
manual_time = time.time() - start
approaches['Manual Loop'] = manual_time
print(f"Manual loop time: {manual_time:.6f} seconds")
print(f"Result size: {len(manual_result)} keys")

# 3. Dictionary comprehension approach
print("\n--- Testing Dictionary comprehension approach ---")
start = time.time()
all_keys = set().union(*[d.keys() for d in large_dicts])
comprehension_result = {key: sum(d.get(key, 0) for d in large_dicts) for key in all_keys}
comprehension_time = time.time() - start
approaches['Dict Comprehension'] = comprehension_time
print(f"Dict comprehension time: {comprehension_time:.6f} seconds")
print(f"Result size: {len(comprehension_result)} keys")

# 4. Reduce with Counter
print("\n--- Testing Reduce approach ---")
from functools import reduce
start = time.time()
reduce_result = dict(reduce(lambda x, y: x + Counter(y), large_dicts, Counter()))
reduce_time = time.time() - start
approaches['Reduce'] = reduce_time
print(f"Reduce time: {reduce_time:.6f} seconds")
print(f"Result size: {len(reduce_result)} keys")

# Verify all results are the same
print(f"\nAll results identical: {counter_result == manual_result == comprehension_result == reduce_result}")

# Performance summary
print("\n=== PERFORMANCE SUMMARY ===")
print(f"{'Approach':<20} {'Time (s)':<12} {'Speedup':<10}")
print("-" * 42)

# Sort by speed (fastest first)
sorted_approaches = sorted(approaches.items(), key=lambda x: x[1])
fastest_time = sorted_approaches[0][1]

for approach, time_taken in sorted_approaches:
    speedup = fastest_time / time_taken
    print(f"{approach:<20} {time_taken:<12.6f} {speedup:<10.2f}x")

print(f"\nFastest approach: {sorted_approaches[0][0]}")
print(f"Slowest approach: {sorted_approaches[-1][0]}")
print(f"Performance difference: {sorted_approaches[-1][1]/sorted_approaches[0][1]:.1f}x")

# Memory usage comparison
import sys

print("\n=== MEMORY USAGE COMPARISON ===")
print("Memory usage for 1000-key dictionaries:")

# Test memory usage
test_dicts = generate_large_dicts(num_dicts=5, dict_size=1000, overlap_ratio=0.2)

# Counter approach memory
import gc
gc.collect()
start_mem = sys.getsizeof(test_dicts)
counter_mem = dict(sum(map(Counter, test_dicts), Counter()))
end_mem = sys.getsizeof(counter_mem)
print(f"Counter approach memory: {end_mem} bytes")

# Manual approach memory
gc.collect()
manual_mem = {}
for d in test_dicts:
    for key, value in d.items():
        manual_mem[key] = manual_mem.get(key, 0) + value
manual_mem_size = sys.getsizeof(manual_mem)
print(f"Manual approach memory: {manual_mem_size} bytes")

# Scalability test
print("\n=== SCALABILITY TEST ===")
sizes = [100, 500, 1000, 2000, 5000]
counter_times = []
manual_times = []

for size in sizes:
    test_dicts = generate_large_dicts(num_dicts=5, dict_size=size, overlap_ratio=0.3)
    
    # Counter timing
    start = time.time()
    dict(sum(map(Counter, test_dicts), Counter()))
    counter_times.append(time.time() - start)
    
    # Manual timing
    start = time.time()
    result = {}
    for d in test_dicts:
        for key, value in d.items():
            result[key] = result.get(key, 0) + value
    manual_times.append(time.time() - start)

print(f"{'Size':<8} {'Counter (s)':<12} {'Manual (s)':<12} {'Ratio':<8}")
print("-" * 40)
for i, size in enumerate(sizes):
    ratio = manual_times[i] / counter_times[i]
    print(f"{size:<8} {counter_times[i]:<12.6f} {manual_times[i]:<12.6f} {ratio:<8.2f}x")

print("\n=== 9. Counter Limitations ===")

print("Counter only works with:")
print("- Hashable objects (strings, numbers, tuples, etc.)")
print("- Cannot count unhashable objects (lists, dicts, sets)")
print("- Values must be numbers (for arithmetic operations)")

# This would work:
valid_counter = Counter(['a', 'b', 'a', 'c'])
print(f"Valid: {valid_counter}")

# This would NOT work:
# invalid_counter = Counter([['a'], ['b'], ['a']])  # Lists are unhashable 