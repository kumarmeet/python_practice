<<<<<<< HEAD
# 1. Create a tuple with single element
def single_element_tuple(element: int) -> tuple[int]:
    # Create a tuple with a single element
    return element,


# 2. Create a tuple with multiple elements
def multi_element_tuple() -> tuple[int, int, int]:
    # Create a tuple with multiple elements (e.g., 1, 2, 3)
    return 1, 2, 3


# 3. Access an element in a tuple
def access_element(tpl: tuple[int, int, int], index: int) -> int:
    # Access an element at a specific index in the tuple
    return tpl[index]


# 4. Tuple unpacking
def tuple_unpacking(tpl: tuple[int, int, int]) -> tuple[int, int, int]:
    # Unpack a tuple into three variables
    a, b, c = tpl
    return a, b, c


# 5. Swap values using tuple assignment
def swap_values(a: int, b: int) -> tuple[int, int]:
    # Swap two values using tuple assignment
    b, a = a, b
    return a, b


# 6. Count occurrences of an element in a tuple
def count_occurrences(tpl: tuple[int, ...], element: int) -> int:
    # Count how many times an element appears in the tuple
    return tpl.count(element)


# 7. Find the index of an element in a tuple
def find_index(tpl: tuple[int, ...], element: int) -> int:
    # Return the index of the first occurrence of the element
    return list(tpl).index(element)


# 8. Convert a list to a tuple
def list_to_tuple(lst: list[int]) -> tuple[int, ...]:
    # Convert a list to a tuple
    return tuple(lst)


# 9. Convert a tuple to a list
def tuple_to_list(tpl: tuple[int, ...]) -> list[int]:
    # Convert a tuple to a list
    return list(tpl)


# 10. Merge two tuples
def merge_tuples(tpl1: tuple[int, ...], tpl2: tuple[int, ...]) -> tuple[int, ...]:
    # Merge two tuples into one
    return tpl1 + tpl2


# 11. Create a tuple with repeated elements
def repeat_tuple(element: int, times: int) -> tuple[int, ...]:
    # Create a tuple with a repeated element
    return (element,) * times


# 12. Slice a tuple
def slice_tuple(tpl: tuple[int, int, int, int], start: int, end: int) -> tuple[int, ...]:
    # Return a slice of the tuple from start to end
    return tpl[start:end]


# 13. Tuple comprehension
def tuple_comprehension(n: int) -> tuple[int, ...]:
    # Create a tuple of squares of numbers from 0 to n-1 using tuple comprehension
    return (*(x ** 2 for x in range(0, n)),)


# 14. Find the maximum value in a tuple
def max_in_tuple(tpl: tuple[int, ...]) -> int:
    # Find the maximum value in the tuple
    return max(tpl)


# 15. Find the minimum value in a tuple
def min_in_tuple(tpl: tuple[int, ...]) -> int:
    # Find the minimum value in the tuple
    return min(tpl)


# 16. Check if a tuple is empty
def is_empty_tuple(tpl: tuple[int, ...]) -> bool:
    # Check if the tuple is empty
    return len(tpl) == 0


# 17. Concatenate tuples
def concatenate_tuples(tpl1: tuple[int, ...], tpl2: tuple[int, ...]) -> tuple[int, ...]:
    # Concatenate two tuples into one
    return tpl1 + tpl2


# 18. Repeat a tuple
def repeat_tuple_elements(tpl: tuple[int, ...], times: int) -> tuple[int, ...]:
    # Repeat the tuple elements a specified number of times
    return tpl * times


# 19. Find the length of a tuple
def length_of_tuple(tpl: tuple[int, ...]) -> int:
    # Return the length of the tuple
    return len(tpl)


# 20. Create a tuple of tuples
def tuple_of_tuples() -> tuple[tuple[int, int], tuple[int, int]]:
    # Create a tuple containing other tuples
    tp1 = tuple((1, 2))
    tp2 = tuple((3, 4))

    return tp1, tp2


# 21. Check if an element is in a tuple
def element_in_tuple(tpl: tuple[int, ...], element: int) -> bool:
    # Check if the element is in the tuple
    return element in tpl


# 22. Get the first n elements of a tuple
def first_n_elements(tpl: tuple[int, ...], n: int) -> tuple[int, ...]:
    # Return the first n elements of the tuple
    return tpl[:n + 1]


# 23. Get the last n elements of a tuple
def last_n_elements(tpl: tuple[int, ...], n: int) -> tuple[int, ...]:
    # Return the last n elements of the tuple
    return tpl[n:]


# 24. Create a tuple of tuples with incrementing values
def incrementing_tuple(n: int) -> tuple[tuple[int, int]]:
    # Create a tuple of tuples with incrementing values
    return (*(i, i + 1 for i in range(n)),)


# 25. Flatten a tuple of tuples
def flatten_tuple_of_tuples(tpl: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    # Flatten a tuple of tuples into a single tuple
    return tuple(item for subtuple in tpl for item in subtuple)


# 26. Convert a tuple to a set
def tuple_to_set(tpl: tuple[int, ...]) -> set[int]:
    # Convert a tuple to a set
    return set(tpl)


# 27. Convert a set to a tuple
def set_to_tuple(s: set[int]) -> tuple[int, ...]:
    # Convert a set to a tuple
    return tuple(s)


# 28. Create a tuple with mixed data types
def mixed_data_types_tuple() -> tuple[int, str, float]:
    # Create a tuple with different data types (int, str, float)
    return 10, "hello", 10.44


# 29. Create a tuple of tuples with indices
def tuple_with_indices(tpl: tuple[str, ...]) -> tuple[tuple[int, str], ...]:
    # Create a tuple of tuples where each inner tuple contains an index and an element
    return (*(i, idx for i, idx in enumerate(tpl)),)


# 30. Check if two tuples are equal
def are_tuples_equal(tpl1: tuple[int, ...], tpl2: tuple[int, ...]) -> bool:
    # Check if two tuples are equal
    return tpl1 == tpl2


# 31. Count the number of tuples in a list of tuples
def count_tuples(lst: list[tuple[int, ...]]) -> int:
    # Count the number of tuples in a list of tuples
    return len(lst)


# 32. Find the longest tuple in a list of tuples
def longest_tuple(lst: list[tuple[int, ...]]) -> tuple[int, ...]:
    # Find the longest tuple in a list of tuples
    return max(lst, key=len)


# 33. Create a tuple with alternating values
def alternating_tuple(n: int) -> tuple[int, ...]:
    # Create a tuple with alternating values (e.g., 1, 0, 1, 0, ...)
    return tuple((i % 2) for i in range(n))


# 34. Create a tuple from a dictionary's items
def dict_to_tuple(d: dict[str, int]) -> tuple[tuple[str, int], ...]:
    # Create a tuple of (key, value) pairs from a dictionary's items
    return (*((key, value) for key, value in d.items()),)


# 35. Find all tuples where the sum of elements equals a target value
def tuples_with_sum(lst: list[tuple[int, int]], target: int) -> list[tuple[int, int]]:
    # Find all tuples in the list where the sum of elements equals the target value
    return [(*(x for x in lst if sum(x) == target))]


# 36. Create a tuple from user input
def tuple_from_input() -> tuple[int, ...]:
    # Create a tuple by taking user input
    ip = input("input values")

    return tuple(map(int, ip.split("")))


# 37. Sum all elements in a tuple
def sum_of_tuple_elements(tpl: tuple[int, ...]) -> int:
    # Sum all elements in the tuple
    return sum(tpl)


# 38. Create a tuple with elements in reverse order
def reverse_tuple(tpl: tuple[int, ...]) -> tuple[int, ...]:
    # Reverse the order of elements in the tuple
    return tuple(reversed(tpl))


# 39. Count the occurrences of each element in a tuple
def count_element_occurrences(tpl: tuple[int, ...]) -> dict[int, int]:
    # Count the occurrences of each element in the tuple
    dc = {}

    for i in tpl:
        if i in tpl:
            dc[i] += 1
        else:
            dc[i] = 1

    return dc


# 40. Filter tuples based on a condition
def filter_tuples(lst: list[tuple[int, int]], condition: callable) -> list[tuple[int, int]]:
    # Filter tuples in the list based on a given condition function
    return list(filter(condition, lst))
=======
# 1. Create a tuple with single element
def single_element_tuple(element: int) -> tuple[int]:
    # Create a tuple with a single element
    return element,


# 2. Create a tuple with multiple elements
def multi_element_tuple() -> tuple[int, int, int]:
    # Create a tuple with multiple elements (e.g., 1, 2, 3)
    return 1, 2, 3


# 3. Access an element in a tuple
def access_element(tpl: tuple[int, int, int], index: int) -> int:
    # Access an element at a specific index in the tuple
    return tpl[index]


# 4. Tuple unpacking
def tuple_unpacking(tpl: tuple[int, int, int]) -> tuple[int, int, int]:
    # Unpack a tuple into three variables
    a, b, c = tpl
    return a, b, c


# 5. Swap values using tuple assignment
def swap_values(a: int, b: int) -> tuple[int, int]:
    # Swap two values using tuple assignment
    b, a = a, b
    return a, b


# 6. Count occurrences of an element in a tuple
def count_occurrences(tpl: tuple[int, ...], element: int) -> int:
    # Count how many times an element appears in the tuple
    return tpl.count(element)


# 7. Find the index of an element in a tuple
def find_index(tpl: tuple[int, ...], element: int) -> int:
    # Return the index of the first occurrence of the element
    return list(tpl).index(element)


# 8. Convert a list to a tuple
def list_to_tuple(lst: list[int]) -> tuple[int, ...]:
    # Convert a list to a tuple
    return tuple(lst)


# 9. Convert a tuple to a list
def tuple_to_list(tpl: tuple[int, ...]) -> list[int]:
    # Convert a tuple to a list
    return list(tpl)


# 10. Merge two tuples
def merge_tuples(tpl1: tuple[int, ...], tpl2: tuple[int, ...]) -> tuple[int, ...]:
    # Merge two tuples into one
    return tpl1 + tpl2


# 11. Create a tuple with repeated elements
def repeat_tuple(element: int, times: int) -> tuple[int, ...]:
    # Create a tuple with a repeated element
    return (element,) * times


# 12. Slice a tuple
def slice_tuple(tpl: tuple[int, int, int, int], start: int, end: int) -> tuple[int, ...]:
    # Return a slice of the tuple from start to end
    return tpl[start:end]


# 13. Tuple comprehension
def tuple_comprehension(n: int) -> tuple[int, ...]:
    # Create a tuple of squares of numbers from 0 to n-1 using tuple comprehension
    return (*(x ** 2 for x in range(0, n)),)


# 14. Find the maximum value in a tuple
def max_in_tuple(tpl: tuple[int, ...]) -> int:
    # Find the maximum value in the tuple
    return max(tpl)


# 15. Find the minimum value in a tuple
def min_in_tuple(tpl: tuple[int, ...]) -> int:
    # Find the minimum value in the tuple
    return min(tpl)


# 16. Check if a tuple is empty
def is_empty_tuple(tpl: tuple[int, ...]) -> bool:
    # Check if the tuple is empty
    return len(tpl) == 0


# 17. Concatenate tuples
def concatenate_tuples(tpl1: tuple[int, ...], tpl2: tuple[int, ...]) -> tuple[int, ...]:
    # Concatenate two tuples into one
    return tpl1 + tpl2


# 18. Repeat a tuple
def repeat_tuple_elements(tpl: tuple[int, ...], times: int) -> tuple[int, ...]:
    # Repeat the tuple elements a specified number of times
    return tpl * times


# 19. Find the length of a tuple
def length_of_tuple(tpl: tuple[int, ...]) -> int:
    # Return the length of the tuple
    return len(tpl)


# 20. Create a tuple of tuples
def tuple_of_tuples() -> tuple[tuple[int, int], tuple[int, int]]:
    # Create a tuple containing other tuples
    tp1 = tuple((1, 2))
    tp2 = tuple((3, 4))

    return tp1, tp2


# 21. Check if an element is in a tuple
def element_in_tuple(tpl: tuple[int, ...], element: int) -> bool:
    # Check if the element is in the tuple
    return element in tpl


# 22. Get the first n elements of a tuple
def first_n_elements(tpl: tuple[int, ...], n: int) -> tuple[int, ...]:
    # Return the first n elements of the tuple
    return tpl[:n + 1]


# 23. Get the last n elements of a tuple
def last_n_elements(tpl: tuple[int, ...], n: int) -> tuple[int, ...]:
    # Return the last n elements of the tuple
    return tpl[n:]


# 24. Create a tuple of tuples with incrementing values
def incrementing_tuple(n: int) -> tuple[tuple[int, int]]:
    # Create a tuple of tuples with incrementing values
    return (*(i, i + 1 for i in range(n)),)


# 25. Flatten a tuple of tuples
def flatten_tuple_of_tuples(tpl: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    # Flatten a tuple of tuples into a single tuple
    return tuple(item for subtuple in tpl for item in subtuple)


# 26. Convert a tuple to a set
def tuple_to_set(tpl: tuple[int, ...]) -> set[int]:
    # Convert a tuple to a set
    return set(tpl)


# 27. Convert a set to a tuple
def set_to_tuple(s: set[int]) -> tuple[int, ...]:
    # Convert a set to a tuple
    return tuple(s)


# 28. Create a tuple with mixed data types
def mixed_data_types_tuple() -> tuple[int, str, float]:
    # Create a tuple with different data types (int, str, float)
    return 10, "hello", 10.44


# 29. Create a tuple of tuples with indices
def tuple_with_indices(tpl: tuple[str, ...]) -> tuple[tuple[int, str], ...]:
    # Create a tuple of tuples where each inner tuple contains an index and an element
    return (*(i, idx for i, idx in enumerate(tpl)),)


# 30. Check if two tuples are equal
def are_tuples_equal(tpl1: tuple[int, ...], tpl2: tuple[int, ...]) -> bool:
    # Check if two tuples are equal
    return tpl1 == tpl2


# 31. Count the number of tuples in a list of tuples
def count_tuples(lst: list[tuple[int, ...]]) -> int:
    # Count the number of tuples in a list of tuples
    return len(lst)


# 32. Find the longest tuple in a list of tuples
def longest_tuple(lst: list[tuple[int, ...]]) -> tuple[int, ...]:
    # Find the longest tuple in a list of tuples
    return max(lst, key=len)


# 33. Create a tuple with alternating values
def alternating_tuple(n: int) -> tuple[int, ...]:
    # Create a tuple with alternating values (e.g., 1, 0, 1, 0, ...)
    return tuple((i % 2) for i in range(n))


# 34. Create a tuple from a dictionary's items
def dict_to_tuple(d: dict[str, int]) -> tuple[tuple[str, int], ...]:
    # Create a tuple of (key, value) pairs from a dictionary's items
    return (*((key, value) for key, value in d.items()),)


# 35. Find all tuples where the sum of elements equals a target value
def tuples_with_sum(lst: list[tuple[int, int]], target: int) -> list[tuple[int, int]]:
    # Find all tuples in the list where the sum of elements equals the target value
    return [(*(x for x in lst if sum(x) == target))]


# 36. Create a tuple from user input
def tuple_from_input() -> tuple[int, ...]:
    # Create a tuple by taking user input
    ip = input("input values")

    return tuple(map(int, ip.split("")))


# 37. Sum all elements in a tuple
def sum_of_tuple_elements(tpl: tuple[int, ...]) -> int:
    # Sum all elements in the tuple
    return sum(tpl)


# 38. Create a tuple with elements in reverse order
def reverse_tuple(tpl: tuple[int, ...]) -> tuple[int, ...]:
    # Reverse the order of elements in the tuple
    return tuple(reversed(tpl))


# 39. Count the occurrences of each element in a tuple
def count_element_occurrences(tpl: tuple[int, ...]) -> dict[int, int]:
    # Count the occurrences of each element in the tuple
    dc = {}

    for i in tpl:
        if i in tpl:
            dc[i] += 1
        else:
            dc[i] = 1

    return dc


# 40. Filter tuples based on a condition
def filter_tuples(lst: list[tuple[int, int]], condition: callable) -> list[tuple[int, int]]:
    # Filter tuples in the list based on a given condition function
    return list(filter(condition, lst))
>>>>>>> 97ed5d77ef971ade0973f4b0714a4aeb250c0bf4
