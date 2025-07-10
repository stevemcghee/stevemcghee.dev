#!/usr/bin/env python3
"""
Code golf solution for combining dictionaries by summing values for duplicate keys.
"""

# Test dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}
dict3 = {'a': 7, 'c': 8, 'e': 9}

print("Original dictionaries:")
print(f"dict1: {dict1}")
print(f"dict2: {dict2}")
print(f"dict3: {dict3}")

# Code golf solution - Strategy 2 (sum values for duplicate keys)
# Smallest possible solution:
from collections import Counter
result = dict(sum(map(Counter, [dict1, dict2, dict3]), Counter()))

print(f"\nCombined (sum values): {result}")

# Even smaller (if you don't need Counter import):
# result = {}
# for d in [dict1, dict2, dict3]:
#     for k,v in d.items(): result[k] = result.get(k,0) + v

# One-liner without Counter:
# result = {k: sum(d.get(k,0) for d in [dict1, dict2, dict3]) for k in set().union(*[d.keys() for d in [dict1, dict2, dict3]])}

# Smallest one-liner with Counter:
# result = dict(sum(map(Counter, [dict1, dict2, dict3]), Counter())) 