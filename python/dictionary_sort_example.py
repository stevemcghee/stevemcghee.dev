#!/usr/bin/env python3
"""
Example demonstrating how to create a dictionary and sort it by value in Python.
"""

def main():
    # Example 1: Simple dictionary with numbers
    print("=== Example 1: Simple number dictionary ===")
    scores = {
        'Alice': 85,
        'Bob': 92,
        'Charlie': 78,
        'Diana': 95,
        'Eve': 88
    }
    
    print("Original dictionary:")
    print(scores)
    
    # Sort by value (ascending)
    sorted_scores_asc = dict(sorted(scores.items(), key=lambda x: x[1]))
    print("\nSorted by value (ascending):")
    print(sorted_scores_asc)
    
    # Sort by value (descending)
    sorted_scores_desc = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
    print("\nSorted by value (descending):")
    print(sorted_scores_desc)
    
    # Example 2: Dictionary with strings
    print("\n=== Example 2: String length dictionary ===")
    words = {
        'apple': 5,
        'banana': 6,
        'cherry': 6,
        'date': 4,
        'elderberry': 11
    }
    
    print("Original dictionary:")
    print(words)
    
    # Sort by value (ascending)
    sorted_words = dict(sorted(words.items(), key=lambda x: x[1]))
    print("\nSorted by word length (ascending):")
    print(sorted_words)
    
    # Example 3: Dictionary with tuples as values
    print("\n=== Example 3: Tuple values dictionary ===")
    students = {
        'John': (85, 'A'),
        'Sarah': (92, 'A'),
        'Mike': (78, 'C'),
        'Lisa': (95, 'A'),
        'Tom': (88, 'B')
    }
    
    print("Original dictionary:")
    print(students)
    
    # Sort by first element of tuple (score)
    sorted_by_score = dict(sorted(students.items(), key=lambda x: x[1][0]))
    print("\nSorted by score (ascending):")
    print(sorted_by_score)
    
    # Sort by second element of tuple (grade)
    sorted_by_grade = dict(sorted(students.items(), key=lambda x: x[1][1]))
    print("\nSorted by grade (alphabetical):")
    print(sorted_by_grade)
    
    # Example 4: Using itemgetter for cleaner code
    print("\n=== Example 4: Using itemgetter ===")
    from operator import itemgetter
    
    prices = {
        'laptop': 1200,
        'phone': 800,
        'tablet': 500,
        'headphones': 150,
        'keyboard': 100
    }
    
    print("Original dictionary:")
    print(prices)
    
    # Sort by value using itemgetter
    sorted_prices = dict(sorted(prices.items(), key=itemgetter(1)))
    print("\nSorted by price (ascending):")
    print(sorted_prices)
    
    # Example 5: Sorting with custom function
    print("\n=== Example 5: Custom sorting function ===")
    
    def sort_by_absolute_value(item):
        """Sort by absolute value of the number"""
        return abs(item[1])
    
    mixed_numbers = {
        'a': -5,
        'b': 3,
        'c': -8,
        'd': 1,
        'e': 7
    }
    
    print("Original dictionary:")
    print(mixed_numbers)
    
    # Sort by absolute value
    sorted_abs = dict(sorted(mixed_numbers.items(), key=sort_by_absolute_value))
    print("\nSorted by absolute value:")
    print(sorted_abs)
    
    # Example 6: Sorting without lambda using operator functions
    print("\n=== Example 6: Sorting without lambda ===")
    
    # Using operator.itemgetter for simple value sorting
    from operator import itemgetter
    
    temperatures = {
        'New York': 72,
        'Los Angeles': 85,
        'Chicago': 65,
        'Miami': 88,
        'Seattle': 58
    }
    
    print("Original dictionary:")
    print(temperatures)
    
    # Sort by value using itemgetter (no lambda)
    sorted_temps = dict(sorted(temperatures.items(), key=itemgetter(1)))
    print("\nSorted by temperature (ascending):")
    print(sorted_temps)
    
    # Example 7: Using custom functions instead of lambda
    print("\n=== Example 7: Custom functions instead of lambda ===")
    
    def get_value(item):
        """Extract the value from a key-value pair"""
        return item[1]
    
    def get_second_char(item):
        """Get the second character of the key"""
        return item[0][1] if len(item[0]) > 1 else ''
    
    def get_value_length(item):
        """Get the length of the value (if it's a string)"""
        return len(str(item[1]))
    
    cities = {
        'Austin': 'Texas',
        'Boston': 'Massachusetts', 
        'Denver': 'Colorado',
        'Phoenix': 'Arizona',
        'Portland': 'Oregon'
    }
    
    print("Original dictionary:")
    print(cities)
    
    # Sort by value using custom function
    sorted_by_state = dict(sorted(cities.items(), key=get_value))
    print("\nSorted by state name:")
    print(sorted_by_state)
    
    # Sort by second character of city name
    sorted_by_second_char = dict(sorted(cities.items(), key=get_second_char))
    print("\nSorted by second character of city name:")
    print(sorted_by_second_char)
    
    # Sort by length of state name
    sorted_by_length = dict(sorted(cities.items(), key=get_value_length))
    print("\nSorted by length of state name:")
    print(sorted_by_length)
    
    # Example 8: Using attrgetter for object attributes
    print("\n=== Example 8: Using attrgetter for objects ===")
    
    from operator import attrgetter
    
    class Person:
        def __init__(self, name, age, city):
            self.name = name
            self.age = age
            self.city = city
        
        def __repr__(self):
            return f"Person({self.name}, {self.age}, {self.city})"
    
    people_dict = {
        'p1': Person('Alice', 30, 'New York'),
        'p2': Person('Bob', 25, 'Los Angeles'),
        'p3': Person('Charlie', 35, 'Chicago'),
        'p4': Person('Diana', 28, 'Miami')
    }
    
    print("Original dictionary:")
    for key, person in people_dict.items():
        print(f"  {key}: {person}")
    
    # Sort by age using custom function (no lambda)
    def get_age(item):
        """Get the age attribute from a person object"""
        return item[1].age
    
    sorted_by_age = dict(sorted(people_dict.items(), key=get_age))
    print("\nSorted by age (using custom function):")
    for key, person in sorted_by_age.items():
        print(f"  {key}: {person}")
    
    # Sort by name using custom function
    def get_name(item):
        """Get the name attribute from a person object"""
        return item[1].name
    
    sorted_by_name = dict(sorted(people_dict.items(), key=get_name))
    print("\nSorted by name:")
    for key, person in sorted_by_name.items():
        print(f"  {key}: {person}")
    
    # Example 9: Using methodcaller for method calls
    print("\n=== Example 9: Using methodcaller ===")
    
    from operator import methodcaller
    
    text_dict = {
        'a': 'hello',
        'b': 'world',
        'c': 'python',
        'd': 'programming',
        'e': 'example'
    }
    
    print("Original dictionary:")
    print(text_dict)
    
    # Sort by string length using methodcaller
    sorted_by_length = dict(sorted(text_dict.items(), key=lambda x: len(x[1])))
    print("\nSorted by length (using lambda):")
    print(sorted_by_length)
    
    # Sort by string length using custom function (no lambda)
    def get_string_length(item):
        """Get the length of the string value"""
        return len(item[1])
    
    sorted_by_length_no_lambda = dict(sorted(text_dict.items(), key=get_string_length))
    print("\nSorted by length (using custom function):")
    print(sorted_by_length_no_lambda)
    
    # Example 10: Using functools.partial
    print("\n=== Example 10: Using functools.partial ===")
    
    from functools import partial
    
    def multiply_by_factor(factor, value):
        """Multiply a value by a factor"""
        return value * factor
    
    numbers_dict = {
        'a': 5,
        'b': 10,
        'c': 3,
        'd': 8,
        'e': 1
    }
    
    print("Original dictionary:")
    print(numbers_dict)
    
    # Sort by value multiplied by 2 using partial
    multiply_by_2 = partial(multiply_by_factor, 2)
    
    def get_multiplied_value(item):
        """Get the value multiplied by 2"""
        return multiply_by_2(item[1])
    
    sorted_by_multiplied = dict(sorted(numbers_dict.items(), key=get_multiplied_value))
    print("\nSorted by value * 2:")
    print(sorted_by_multiplied)
    
    # Example 11: Combining multiple dictionaries and getting top 10 values
    print("\n=== Example 11: Combining multiple dictionaries ===")
    
    # Multiple dictionaries with different data
    dict1 = {
        'apple': 15,
        'banana': 8,
        'cherry': 12,
        'date': 5,
        'elderberry': 20
    }
    
    dict2 = {
        'fig': 18,
        'grape': 10,
        'honeydew': 7,
        'kiwi': 14,
        'lemon': 9
    }
    
    dict3 = {
        'mango': 22,
        'nectarine': 11,
        'orange': 16,
        'peach': 13,
        'quince': 6
    }
    
    print("Dictionary 1:")
    print(dict1)
    print("\nDictionary 2:")
    print(dict2)
    print("\nDictionary 3:")
    print(dict3)
    
    # Method 1: Using dict.update() to combine
    print("\n--- Method 1: Using dict.update() ---")
    combined_dict = {}
    combined_dict.update(dict1)
    combined_dict.update(dict2)
    combined_dict.update(dict3)
    
    print("Combined dictionary:")
    print(combined_dict)
    
    # Get top 10 by value (descending)
    def get_value_for_sorting(item):
        """Get the value for sorting"""
        return item[1]
    
    top_10_items = sorted(combined_dict.items(), key=get_value_for_sorting, reverse=True)[:10]
    top_10_dict = dict(top_10_items)
    
    print("\nTop 10 items by value (descending):")
    print(top_10_dict)
    
    # Method 2: Using | operator (Python 3.9+)
    print("\n--- Method 2: Using | operator ---")
    combined_dict_2 = dict1 | dict2 | dict3
    
    print("Combined dictionary using | operator:")
    print(combined_dict_2)
    
    # Get top 10 using itemgetter
    from operator import itemgetter
    top_10_items_2 = sorted(combined_dict_2.items(), key=itemgetter(1), reverse=True)[:10]
    top_10_dict_2 = dict(top_10_items_2)
    
    print("\nTop 10 items by value (descending):")
    print(top_10_dict_2)
    
    # Method 3: Using collections.ChainMap
    print("\n--- Method 3: Using collections.ChainMap ---")
    from collections import ChainMap
    
    chain_dict = ChainMap(dict1, dict2, dict3)
    
    print("Combined dictionary using ChainMap:")
    print(dict(chain_dict))
    
    # Get top 10 from ChainMap
    top_10_items_3 = sorted(chain_dict.items(), key=itemgetter(1), reverse=True)[:10]
    top_10_dict_3 = dict(top_10_items_3)
    
    print("\nTop 10 items by value (descending):")
    print(top_10_dict_3)
    
    # Method 4: Using dict comprehension with multiple sources
    print("\n--- Method 4: Using dict comprehension ---")
    
    # List of dictionaries
    dict_list = [dict1, dict2, dict3]
    
    # Combine using dict comprehension
    combined_dict_4 = {k: v for d in dict_list for k, v in d.items()}
    
    print("Combined dictionary using comprehension:")
    print(combined_dict_4)
    
    # Get top 10 with custom function
    def get_value_descending(item):
        """Get negative value for descending sort without reverse=True"""
        return -item[1]
    
    top_10_items_4 = sorted(combined_dict_4.items(), key=get_value_descending)[:10]
    top_10_dict_4 = dict(top_10_items_4)
    
    print("\nTop 10 items by value (descending):")
    print(top_10_dict_4)
    
    # Method 5: Using heapq for top N values (more efficient for large datasets)
    print("\n--- Method 5: Using heapq for efficiency ---")
    import heapq
    
    # Combine dictionaries
    combined_dict_5 = {**dict1, **dict2, **dict3}
    
    print("Combined dictionary using ** unpacking:")
    print(combined_dict_5)
    
    # Get top 10 using heapq.nlargest (most efficient for large datasets)
    def get_value_for_heapq(item):
        """Get value for heapq sorting"""
        return item[1]
    
    top_10_items_5 = heapq.nlargest(10, combined_dict_5.items(), key=get_value_for_heapq)
    top_10_dict_5 = dict(top_10_items_5)
    
    print("\nTop 10 items by value (using heapq):")
    print(top_10_dict_5)
    
    # Method 6: Handling duplicate keys with different strategies
    print("\n--- Method 6: Handling duplicate keys ---")
    
    # Dictionaries with potential duplicate keys
    dict_a = {'apple': 15, 'banana': 8, 'cherry': 12}
    dict_b = {'apple': 25, 'grape': 10, 'kiwi': 14}  # apple has different value
    dict_c = {'mango': 22, 'banana': 18, 'peach': 13}  # banana has different value
    
    print("Dictionary A:")
    print(dict_a)
    print("\nDictionary B:")
    print(dict_b)
    print("\nDictionary C:")
    print(dict_c)
    
    # Strategy 1: Last value wins (default behavior)
    combined_last_wins = {**dict_a, **dict_b, **dict_c}
    print("\nCombined (last value wins):")
    print(combined_last_wins)
    
    # Strategy 2: Sum values for duplicate keys
    def combine_with_sum(dicts):
        """Combine dictionaries by summing values for duplicate keys"""
        result = {}
        for d in dicts:
            for key, value in d.items():
                result[key] = result.get(key, 0) + value
        return result
    
    combined_sum = combine_with_sum([dict_a, dict_b, dict_c])
    print("\nCombined (sum values):")
    print(combined_sum)
    
    # Get top 5 from summed values
    top_5_summed = dict(sorted(combined_sum.items(), key=itemgetter(1), reverse=True)[:5])
    print("\nTop 5 items by summed values:")
    print(top_5_summed)

if __name__ == "__main__":
    main() 