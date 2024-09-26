# 1. Create a list of numbers from 1 to 10
def create_list() -> list[int]:
    # Declare a list of numbers from 1 to 10
    l1: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return l1


# 2. Create a list using range
def list_with_range() -> list[int]:
    # Create a list using the range() function from 0 to 9
    l1: list[int] = []

    for i in range(0, 10):
        l1.append(i)

    return l1


# 3. Append an element to a list
def append_to_list(lst: list[int], element: int) -> None:
    # Append an element to the list
    lst.append(element)


# 4. Remove an element from a list
def remove_from_list(lst: list[int], element: int) -> None:
    # Remove the first occurrence of the element from the list
    lst.remove(element)


# 5. Insert an element at a specific index
def insert_at_index(lst: list[int], index: int, element: int) -> None:
    # Insert an element at a specific index in the list
    lst.insert(index, element)


# 6. Find the length of a list
def get_length(lst: list[int]) -> int:
    # Return the length of the list
    return len(lst)


# 7. List comprehension to create squares of numbers from 1 to 10
def squares_of_numbers() -> list[int]:
    # Create a list of squares of numbers from 1 to 10 using list comprehension
    lst: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return [x ** 2 for x in lst]


# 8. Filter even numbers using list comprehension
def filter_even_numbers(lst: list[int]) -> list[int]:
    # Filter the even numbers from a list using list comprehension
    return [x for x in lst if x % 2 == 0]


# 9. Flatten a 2D list using list comprehension
def flatten_2d_list(lst: list[list[int]]) -> list[int]:
    # Flatten a 2D list into a 1D list using list comprehension
    return [item for sublist in lst for item in sublist]


# 10. List comprehension with conditional
def squares_of_odd_numbers(lst: list[int]) -> list[int]:
    # Return the squares of only odd numbers using list comprehension
    return [x ** 2 for x in lst if x % 2 != 0]


# 11. Multiply all elements in a list by 2
def multiply_by_two(lst: list[int]) -> list[int]:
    # Multiply each element in the list by 2
    return [x * 2 for x in lst]


# 12. Sort a list in ascending order
def sort_list(lst: list[int]) -> list[int]:
    # Return the list sorted in ascending order
    return sorted(lst)


# 13. Reverse a list
def reverse_list(lst: list[int]) -> list[int]:
    # Return the list in reverse order
    return lst[::-1]


# 14. Find the minimum value in a list
def find_minimum(lst: list[int]) -> int:
    # Return the minimum value in the list
    return min(lst)


# 15. Find the maximum value in a list
def find_maximum(lst: list[int]) -> int:
    # Return the maximum value in the list
    return max(lst)


# 16. Check if a list is empty
def is_empty(lst: list[int]) -> bool:
    # Check if the list is empty
    return len(lst) == 0


# 17. Concatenate two lists
def concatenate_lists(lst1: list[int], lst2: list[int]) -> list[int]:
    # Concatenate two lists into one
    return lst1 + lst2


# 18. Create a list of tuples (number, square) using list comprehension
def create_tuples_of_squares() -> list[tuple[int, int]]:
    # Return a list of tuples where each tuple contains (number, square)
    lst: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return [(i, i ** 2) for i in lst]


# 19. Remove duplicates from a list
def remove_duplicates(lst: list[int]) -> list[int]:
    # Remove duplicates from the list and return the result
    return list(set(lst))


# 20. Find the index of an element in a list
def find_index(lst: list[int], element: int) -> int:
    # Return the index of the element in the list
    return lst.index(element)


# 21. Check if an element exists in a list
def element_exists(lst: list[int], element: int) -> bool:
    # Return True if the element exists in the list, False otherwise
    return element in lst


# 22. Create a list of lists (matrix)
def create_matrix(rows: int, cols: int) -> list[list[int]]:
    # Create a matrix (list of lists) with the given number of rows and columns
    lst: list[list[int]] = []

    for i in range(cols):
        row = []
        for j in range(rows):
            row.append(j)
        lst.append(row)

    return lst


# 23. Transpose a matrix (2D list)
def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    # Transpose the given matrix (swap rows and columns)
    return [list(row) for row in zip(*matrix)]


# 24. Split a list into chunks of a specific size
def split_into_chunks(lst: list[int], chunk_size: int) -> list[list[int]]:
    # Split the list into chunks of the given size
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


# 25. Create a list of powers of 2 using list comprehension
def powers_of_two(n: int) -> list[int]:
    # Return a list of powers of 2 up to 2^n using list comprehension
    return [2 ** x for x in range(n + 1)]


# 26. Filter out negative numbers from a list
def filter_negatives(lst: list[int]) -> list[int]:
    # Return a list with only positive numbers (remove negative numbers)
    return [x for x in lst if x >= 0]


# 27. Find common elements between two lists
def common_elements(lst1: list[int], lst2: list[int]) -> list[int]:
    # Return a list of common elements between two lists
    return list(set(lst1) & set(lst2))


# 28. Sum of all elements in a list
def sum_of_elements(lst: list[int]) -> int:
    # Return the sum of all elements in the list
    return sum(lst)


# 29. Count the occurrences of an element in a list
def count_occurrences(lst: list[int], element: int) -> int:
    # Count how many times an element appears in the list
    return lst.count(element)


# 30. Remove the smallest element from a list
def remove_smallest(lst: list[int]) -> list[int]:
    # Remove the smallest element from the list and return the result
    smallest = min(lst)

    lst.remove(smallest)

    return lst
