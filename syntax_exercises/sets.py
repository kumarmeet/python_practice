from itertools import combinations


# 1. Create an empty set
def create_empty_set() -> set[int]:
    # Create and return an empty set
    return set()


# 2. Create a set with multiple elements
def create_set_with_elements() -> set[int]:
    # Create a set with multiple elements (e.g., {1, 2, 3})
    return {1, 2, 3}


# 3. Add an element to a set
def add_element_to_set(s: set[int], element: int) -> None:
    # Add an element to the set
    s.add(element)


# 4. Remove an element from a set
def remove_element_from_set(s: set[int], element: int) -> None:
    # Remove an element from the set
    s.remove(element)


# 5. Check if an element is in a set
def element_in_set(s: set[int], element: int) -> bool:
    # Check if an element is in the set
    return element in s


# 6. Find the length of a set
def length_of_set(s: set[int]) -> int:
    # Return the number of elements in the set
    return len(s)


# 7. Union of two sets
def union_of_sets(s1: set[int], s2: set[int]) -> set[int]:
    # Return the union of two sets
    return s1 | s2


# 8. Intersection of two sets
def intersection_of_sets(s1: set[int], s2: set[int]) -> set[int]:
    # Return the intersection of two sets
    return s1 & s2


# 9. Difference of two sets
def difference_of_sets(s1: set[int], s2: set[int]) -> set[int]:
    # Return the difference between two sets
    return s1 - s2


# 10. Symmetric difference of two sets
def symmetric_difference_of_sets(s1: set[int], s2: set[int]) -> set[int]:
    # Return the symmetric difference between two sets
    return s1 ^ s2


# 11. Subset check
def is_subset(s1: set[int], s2: set[int]) -> bool:
    # Check if s1 is a subset of s2
    return s1 <= s2


# 12. Superset check
def is_superset(s1: set[int], s2: set[int]) -> bool:
    # Check if s1 is a superset of s2
    return s1 >= s2


# 13. Clear all elements from a set
def clear_set(s: set[int]) -> None:
    # Remove all elements from the set
    s.clear()


# 14. Create a set from a list
def list_to_set(lst: list[int]) -> set[int]:
    # Convert a list to a set
    return set(lst)


# 15. Create a set from a string
def string_to_set(s: str) -> set[str]:
    # Convert a string to a set of characters
    return set(s)


# 16. Remove an element if it exists, otherwise add it
def toggle_element_in_set(s: set[int], element: int) -> None:
    # Remove an element if it exists, otherwise add it to the set
    s.add(element)


# 17. Iterate over elements in a set
def iterate_over_set(s: set[int]) -> list[int]:
    # Return a list of elements in the set (in arbitrary order)
    pass


# 18. Create a set with unique elements from a list
def unique_elements_from_list(lst: list[int]) -> set[int]:
    # Create a set from a list to ensure uniqueness
    return set(lst)


# 19. Create a set of tuples
def create_set_of_tuples() -> set[tuple[int, int]]:
    # Create a set containing tuples (e.g., {(1, 2), (3, 4)})
    return {(1, 2), (4, 6)}


# 20. Check if a set is disjoint with another set
def are_sets_disjoint(s1: set[int], s2: set[int]) -> bool:
    # Check if two sets are disjoint (have no common elements)
    return are_sets_disjoint(s1, s2)


# 21. Find the maximum element in a set
def max_in_set(s: set[int]) -> int:
    # Return the maximum element in the set
    return max(s)


# 22. Find the minimum element in a set
def min_in_set(s: set[int]) -> int:
    # Return the minimum element in the set
    return min(set)


# 23. Convert a set to a tuple
def set_to_tuple(s: set[int]) -> tuple[int, ...]:
    # Convert a set to a tuple
    return tuple(s)


# 24. Convert a tuple to a set
def tuple_to_set(tpl: tuple[int, ...]) -> set[int]:
    # Convert a tuple to a set
    return set(tpl)


# 25. Create a set with elements based on a condition
def set_comprehension(n: int) -> set[int]:
    # Create a set of squares of numbers from 0 to n-1 using set comprehension
    return {x ** 2 for x in range(n)}


# 26. Merge multiple sets into one
def merge_multiple_sets(sets: list[set[int]]) -> set[int]:
    # Merge multiple sets into one
    merged_set = set()

    for s in sets:
        merged_set.update(s)

    return merged_set


# 27. Create a set of even numbers from a list
def even_numbers_from_list(lst: list[int]) -> set[int]:
    # Create a set containing even numbers from the list
    return {x for x in lst if x % 2 == 0}


# 28. Create a set of odd numbers from a list
def odd_numbers_from_list(lst: list[int]) -> set[int]:
    # Create a set containing odd numbers from the list
    return {x for x in lst if x % 2 != 0}


# 29. Create a set with elements from a range
def range_to_set(start: int, end: int) -> set[int]:
    # Create a set from a range of numbers
    return {x for x in range(start, end)}


# 30. Generate all subsets of a set
def subsets_of_set(s: set[int]) -> list[set[int]]:
    # Generate all possible subsets of the set
    subsets = []
    for r in range(len(s) + 1):
        for combo in combinations(s, r):
            subsets.append(set(combo))
    return subsets


# 31. Find the intersection of multiple sets
def intersection_of_multiple_sets(sets: list[set[int]]) -> set[int]:
    # Find the intersection of multiple sets
    return set.intersection(*sets)


# 32. Create a set of unique words from a string
def unique_words_from_string(s: str) -> set[str]:
    # Create a set of unique words from a string
    return set(s.split(" "))


# 33. Find the difference between multiple sets
def difference_of_multiple_sets(sets: list[set[int]]) -> set[int]:
    # Find the difference between multiple sets
    return set.difference(*sets)


# 34. Convert a set of tuples to a set of individual elements
def tuples_to_elements(s: set[tuple[int, int]]) -> set[int]:
    # Convert a set of tuples to a set of individual elements
    return {element for tup in s for element in tup}


# 35. Create a set with the square of each element in another set
def square_elements_in_set(s: set[int]) -> set[int]:
    # Create a set with the square of each element in the given set
    return {x ** 2 for x in s}


# 36. Create a set of unique characters from a list of strings
def unique_chars_from_list_of_strings(lst: list[str]) -> set[str]:
    # Create a set of unique characters from a list of strings
    return {c for s in lst for c in s}


# 37. Create a set from a list with duplicate removal
def remove_duplicates_from_list(lst: list[int]) -> set[int]:
    # Create a set from a list to remove duplicates
    return set(lst)


# 38. Filter a set based on a condition
def filter_set(s: set[int], condition: callable) -> set[int]:
    # Filter elements in the set based on a given condition function
    return set(filter(condition, s))


# 39. Create a set from a dictionary’s keys
def dict_keys_to_set(d: dict[int, str]) -> set[int]:
    # Create a set from the keys of a dictionary
    return set(d.keys())


# 40. Create a set from a dictionary’s values
def dict_values_to_set(d: dict[int, str]) -> set[str]:
    # Create a set from the values of a dictionary
    return set(d.values())
