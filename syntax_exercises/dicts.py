<<<<<<< HEAD
# 1. Create an empty dictionary
from collections import Counter


def create_empty_dict() -> dict[str, int]:
    # Create and return an empty dictionary
    return dict()


# 2. Create a dictionary with initial key-value pairs
def create_dict_with_initial_pairs() -> dict[str, int]:
    # Create a dictionary with initial key-value pairs (e.g., {'a': 1, 'b': 2})
    return {"a": 1, "b": 2}


# 3. Add a key-value pair to a dictionary
def add_key_value_pair(d: dict[str, int], key: str, value: int) -> None:
    # Add a key-value pair to the dictionary
    d[key] = value


# 4. Update the value for an existing key
def update_value(d: dict[str, int], key: str, value: int) -> None:
    # Update the value for a given key in the dictionary
    d.update({key: value})


# 5. Remove a key-value pair from a dictionary
def remove_key(d: dict[str, int], key: str) -> None:
    # Remove a key-value pair from the dictionary
    d.pop(key)


# 6. Get the value for a specific key
def get_value(d: dict[str, int], key: str) -> int:
    # Get the value for a specific key in the dictionary
    return d[key]


# 7. Check if a key exists in the dictionary
def key_exists(d: dict[str, int], key: str) -> bool:
    # Check if a key exists in the dictionary
    return key in d


# 8. Iterate over dictionary keys
def iterate_keys(d: dict[str, int]) -> list[str]:
    # Return a list of keys in the dictionary
    return list(d.keys())


# 9. Iterate over dictionary values
def iterate_values(d: dict[str, int]) -> list[int]:
    # Return a list of values in the dictionary
    return list(d.values())


# 10. Iterate over dictionary key-value pairs
def iterate_items(d: dict[str, int]) -> list[tuple[str, int]]:
    # Return a list of key-value pairs (tuples) in the dictionary
    return [(key, value) for key, value in d.items()]


# 11. Create a dictionary from two lists (keys and values)
def dict_from_lists(keys: list[str], values: list[int]) -> dict[str, int]:
    # Create a dictionary from two lists: keys and values
    return dict(zip(keys, values))


# 12. Merge two dictionaries
def merge_dicts(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:
    # Merge two dictionaries into one
    return {**d1, **d2}


# 13. Get all keys from a dictionary
def get_all_keys(d: dict[str, int]) -> list[str]:
    # Return a list of all keys in the dictionary
    return list(d.keys())


# 14. Get all values from a dictionary
def get_all_values(d: dict[str, int]) -> list[int]:
    # Return a list of all values in the dictionary
    return list(d.values())


# 15. Get a dictionary with keys sorted
def sorted_keys_dict(d: dict[str, int]) -> dict[str, int]:
    # Return a dictionary with keys sorted
    # return dict(sorted(d.items()))
    return {k: d[k] for k in sorted(d)}


# 16. Get a dictionary with values sorted
def sorted_values_dict(d: dict[str, int]) -> dict[str, int]:
    # Return a dictionary with values sorted (keys may be reordered)
    # return {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
    return dict(sorted(d.items(), key=lambda item: item[1]))


# 17. Create a dictionary from a list of tuples
def dict_from_tuples(lst: list[tuple[str, int]]) -> dict[str, int]:
    # Create a dictionary from a list of (key, value) tuples
    return dict(lst)


# 18. Count the number of items in a dictionary
def count_items(d: dict[str, int]) -> int:
    # Return the number of key-value pairs in the dictionary
    pass


# 19. Clear all items from a dictionary
def clear_dict(d: dict[str, int]) -> None:
    # Clear all items from the dictionary
    d.clear()


# 20. Create a dictionary with default values for keys
def default_dict(keys: list[str], default_value: int) -> dict[str, int]:
    # Create a dictionary with keys and default values
    d = {}
    d.setdefault(keys, default_value)
    return d


# 21. Create a dictionary from a string (character frequency)
def string_to_char_freq(s: str) -> dict[str, int]:
    # Create a dictionary with character frequencies from a string
    d1 = {}

    for i in s:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
    return d1


# 22. Create a dictionary from a list of keys with default values
def list_to_dict_with_default(keys: list[str], default_value: int) -> dict[str, int]:
    # Create a dictionary with list of keys and a default value
    return dict.fromkeys(keys, default_value)


# 23. Merge multiple dictionaries
def merge_multiple_dicts(dicts: list[dict[str, int]]) -> dict[str, int]:
    # Merge multiple dictionaries into one
    merged = {}
    for d in dicts:
        merged.update(d)
    return merged


# 24. Get dictionary keys as a set
def dict_keys_as_set(d: dict[str, int]) -> set[str]:
    # Get the keys of the dictionary as a set
    return {k for k, v in d}


# 25. Get dictionary values as a set
def dict_values_as_set(d: dict[str, int]) -> set[int]:
    # Get the values of the dictionary as a set
    return {v for k, v in d}


# 26. Filter a dictionary based on a condition
def filter_dict(d: dict[str, int], condition: callable) -> dict[str, int]:
    # Filter the dictionary based on a condition function
    return dict(filter(condition, d))


# 27. Create a dictionary from a list of lists (key-value pairs)
def list_of_lists_to_dict(lst: list[list[str, int]]) -> dict[str, int]:
    # Create a dictionary from a list of lists where each list contains a key-value pair
    return {k: v for k, v in lst}


# 28. Create a dictionary with cumulative sums of a list
def cumulative_sum_dict(lst: list[int]) -> dict[int, int]:
    # Create a dictionary with cumulative sums of the list elements
    cumulative_sum = 0
    result = {}

    for i, num in enumerate(lst):
        cumulative_sum += num
        result[i] = cumulative_sum

    return result


# 29. Create a dictionary with unique values from a list
def unique_values_dict(lst: list[int]) -> dict[int, None]:
    # Create a dictionary with unique values from the list
    return {value: None for value in set(lst)}


# 30. Group elements of a list by their frequency
def group_by_frequency(lst: list[int]) -> dict[int, int]:
    # Group elements of the list by their frequency and return a dictionary
    return dict(Counter(lst))


# 31. Create a dictionary with values from a string (word frequency)
def string_to_word_freq(s: str) -> dict[str, int]:
    # Create a dictionary with word frequencies from a string
    return dict(Counter(s))


# 32. Merge dictionaries by summing values of common keys
def merge_and_sum_dicts(dicts: list[dict[str, int]]) -> dict[str, int]:
    # Merge dictionaries by summing values of common keys
    merged_dict = {}

    for d in dicts:
        for k, v in d.items():
            if k in merged_dict:
                merged_dict[k] += v
            else:
                merged_dict[k] = v

    return merged_dict


# 33. Convert a dictionary into a list of tuples
def dict_to_list_of_tuples(d: dict[str, int]) -> list[tuple[str, int]]:
    # Convert a dictionary into a list of (key, value) tuples
    return list(d.items())


# 34. Get the key with the maximum value
def key_with_max_value(d: dict[str, int]) -> str:
    # Return the key with the maximum value in the dictionary
    return max(d, key=d.get)


# 35. Get the key with the minimum value
def key_with_min_value(d: dict[str, int]) -> str:
    # Return the key with the minimum value in the dictionary
    return min(d, key=d.get)


# 36. Create a dictionary with conditional values
def conditional_dict(keys: list[str], condition: callable) -> dict[str, int]:
    # Create a dictionary where values are determined by a condition function
    return {k: condition(k) for k in keys}


# 37. Get a dictionary with values incremented by 1
def increment_values(d: dict[str, int]) -> dict[str, int]:
    # Increment all values in the dictionary by 1
    return {k: v + 1 for k, v in d.items()}


# 38. Create a dictionary with reversed key-value pairs
def reverse_key_value_pairs(d: dict[str, int]) -> dict[int, str]:
    # Create a dictionary with reversed key-value pairs
    return {v: k for k, v in d.items()}


# 39. Create a dictionary from a list of keys with index values
def list_keys_with_index(keys: list[str]) -> dict[str, int]:
    # Create a dictionary where keys are from the list and values are their indices
    return {v: i for i, v in enumerate(keys)}


# 40. Merge dictionaries while keeping the first occurrence of each key
def merge_dicts_keep_first(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:
    # Merge two dictionaries, keeping the first occurrence of each key
    result = d1.copy()  # Start with a copy of d1
    for key, value in d2.items():
        if key not in result:  # If key is not already in result, add it
            result[key] = value
    return result
=======
# 1. Create an empty dictionary
from collections import Counter


def create_empty_dict() -> dict[str, int]:
    # Create and return an empty dictionary
    return dict()


# 2. Create a dictionary with initial key-value pairs
def create_dict_with_initial_pairs() -> dict[str, int]:
    # Create a dictionary with initial key-value pairs (e.g., {'a': 1, 'b': 2})
    return {"a": 1, "b": 2}


# 3. Add a key-value pair to a dictionary
def add_key_value_pair(d: dict[str, int], key: str, value: int) -> None:
    # Add a key-value pair to the dictionary
    d[key] = value


# 4. Update the value for an existing key
def update_value(d: dict[str, int], key: str, value: int) -> None:
    # Update the value for a given key in the dictionary
    d.update({key: value})


# 5. Remove a key-value pair from a dictionary
def remove_key(d: dict[str, int], key: str) -> None:
    # Remove a key-value pair from the dictionary
    d.pop(key)


# 6. Get the value for a specific key
def get_value(d: dict[str, int], key: str) -> int:
    # Get the value for a specific key in the dictionary
    return d[key]


# 7. Check if a key exists in the dictionary
def key_exists(d: dict[str, int], key: str) -> bool:
    # Check if a key exists in the dictionary
    return key in d


# 8. Iterate over dictionary keys
def iterate_keys(d: dict[str, int]) -> list[str]:
    # Return a list of keys in the dictionary
    return list(d.keys())


# 9. Iterate over dictionary values
def iterate_values(d: dict[str, int]) -> list[int]:
    # Return a list of values in the dictionary
    return list(d.values())


# 10. Iterate over dictionary key-value pairs
def iterate_items(d: dict[str, int]) -> list[tuple[str, int]]:
    # Return a list of key-value pairs (tuples) in the dictionary
    return [(key, value) for key, value in d.items()]


# 11. Create a dictionary from two lists (keys and values)
def dict_from_lists(keys: list[str], values: list[int]) -> dict[str, int]:
    # Create a dictionary from two lists: keys and values
    return dict(zip(keys, values))


# 12. Merge two dictionaries
def merge_dicts(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:
    # Merge two dictionaries into one
    return {**d1, **d2}


# 13. Get all keys from a dictionary
def get_all_keys(d: dict[str, int]) -> list[str]:
    # Return a list of all keys in the dictionary
    return list(d.keys())


# 14. Get all values from a dictionary
def get_all_values(d: dict[str, int]) -> list[int]:
    # Return a list of all values in the dictionary
    return list(d.values())


# 15. Get a dictionary with keys sorted
def sorted_keys_dict(d: dict[str, int]) -> dict[str, int]:
    # Return a dictionary with keys sorted
    # return dict(sorted(d.items()))
    return {k: d[k] for k in sorted(d)}


# 16. Get a dictionary with values sorted
def sorted_values_dict(d: dict[str, int]) -> dict[str, int]:
    # Return a dictionary with values sorted (keys may be reordered)
    # return {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
    return dict(sorted(d.items(), key=lambda item: item[1]))


# 17. Create a dictionary from a list of tuples
def dict_from_tuples(lst: list[tuple[str, int]]) -> dict[str, int]:
    # Create a dictionary from a list of (key, value) tuples
    return dict(lst)


# 18. Count the number of items in a dictionary
def count_items(d: dict[str, int]) -> int:
    # Return the number of key-value pairs in the dictionary
    pass


# 19. Clear all items from a dictionary
def clear_dict(d: dict[str, int]) -> None:
    # Clear all items from the dictionary
    d.clear()


# 20. Create a dictionary with default values for keys
def default_dict(keys: list[str], default_value: int) -> dict[str, int]:
    # Create a dictionary with keys and default values
    d = {}
    d.setdefault(keys, default_value)
    return d


# 21. Create a dictionary from a string (character frequency)
def string_to_char_freq(s: str) -> dict[str, int]:
    # Create a dictionary with character frequencies from a string
    d1 = {}

    for i in s:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
    return d1


# 22. Create a dictionary from a list of keys with default values
def list_to_dict_with_default(keys: list[str], default_value: int) -> dict[str, int]:
    # Create a dictionary with list of keys and a default value
    return dict.fromkeys(keys, default_value)


# 23. Merge multiple dictionaries
def merge_multiple_dicts(dicts: list[dict[str, int]]) -> dict[str, int]:
    # Merge multiple dictionaries into one
    merged = {}
    for d in dicts:
        merged.update(d)
    return merged


# 24. Get dictionary keys as a set
def dict_keys_as_set(d: dict[str, int]) -> set[str]:
    # Get the keys of the dictionary as a set
    return {k for k, v in d}


# 25. Get dictionary values as a set
def dict_values_as_set(d: dict[str, int]) -> set[int]:
    # Get the values of the dictionary as a set
    return {v for k, v in d}


# 26. Filter a dictionary based on a condition
def filter_dict(d: dict[str, int], condition: callable) -> dict[str, int]:
    # Filter the dictionary based on a condition function
    return dict(filter(condition, d))


# 27. Create a dictionary from a list of lists (key-value pairs)
def list_of_lists_to_dict(lst: list[list[str, int]]) -> dict[str, int]:
    # Create a dictionary from a list of lists where each list contains a key-value pair
    return {k: v for k, v in lst}


# 28. Create a dictionary with cumulative sums of a list
def cumulative_sum_dict(lst: list[int]) -> dict[int, int]:
    # Create a dictionary with cumulative sums of the list elements
    cumulative_sum = 0
    result = {}

    for i, num in enumerate(lst):
        cumulative_sum += num
        result[i] = cumulative_sum

    return result


# 29. Create a dictionary with unique values from a list
def unique_values_dict(lst: list[int]) -> dict[int, None]:
    # Create a dictionary with unique values from the list
    return {value: None for value in set(lst)}


# 30. Group elements of a list by their frequency
def group_by_frequency(lst: list[int]) -> dict[int, int]:
    # Group elements of the list by their frequency and return a dictionary
    return dict(Counter(lst))


# 31. Create a dictionary with values from a string (word frequency)
def string_to_word_freq(s: str) -> dict[str, int]:
    # Create a dictionary with word frequencies from a string
    return dict(Counter(s))


# 32. Merge dictionaries by summing values of common keys
def merge_and_sum_dicts(dicts: list[dict[str, int]]) -> dict[str, int]:
    # Merge dictionaries by summing values of common keys
    merged_dict = {}

    for d in dicts:
        for k, v in d.items():
            if k in merged_dict:
                merged_dict[k] += v
            else:
                merged_dict[k] = v

    return merged_dict


# 33. Convert a dictionary into a list of tuples
def dict_to_list_of_tuples(d: dict[str, int]) -> list[tuple[str, int]]:
    # Convert a dictionary into a list of (key, value) tuples
    return list(d.items())


# 34. Get the key with the maximum value
def key_with_max_value(d: dict[str, int]) -> str:
    # Return the key with the maximum value in the dictionary
    return max(d, key=d.get)


# 35. Get the key with the minimum value
def key_with_min_value(d: dict[str, int]) -> str:
    # Return the key with the minimum value in the dictionary
    return min(d, key=d.get)


# 36. Create a dictionary with conditional values
def conditional_dict(keys: list[str], condition: callable) -> dict[str, int]:
    # Create a dictionary where values are determined by a condition function
    return {k: condition(k) for k in keys}


# 37. Get a dictionary with values incremented by 1
def increment_values(d: dict[str, int]) -> dict[str, int]:
    # Increment all values in the dictionary by 1
    return {k: v + 1 for k, v in d.items()}


# 38. Create a dictionary with reversed key-value pairs
def reverse_key_value_pairs(d: dict[str, int]) -> dict[int, str]:
    # Create a dictionary with reversed key-value pairs
    return {v: k for k, v in d.items()}


# 39. Create a dictionary from a list of keys with index values
def list_keys_with_index(keys: list[str]) -> dict[str, int]:
    # Create a dictionary where keys are from the list and values are their indices
    return {v: i for i, v in enumerate(keys)}


# 40. Merge dictionaries while keeping the first occurrence of each key
def merge_dicts_keep_first(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:
    # Merge two dictionaries, keeping the first occurrence of each key
    result = d1.copy()  # Start with a copy of d1
    for key, value in d2.items():
        if key not in result:  # If key is not already in result, add it
            result[key] = value
    return result
>>>>>>> 97ed5d77ef971ade0973f4b0714a4aeb250c0bf4
