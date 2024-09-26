# Python Syntax Practice: Packing and Unpacking (20 Questions)

# **1. Basic Tuple Unpacking**
# - Unpack a tuple into individual variables.
# - Example: `def unpack_tuple(t: tuple) -> tuple: ...`
# ```python
# def unpack_tuple(t: tuple) -> tuple:
#     a, b, c = t
#     return a, b, c
# ```

# **2. Basic List Unpacking**
# - Unpack a list into individual variables.
# - Example: `def unpack_list(lst: list) -> tuple: ...`
# ```python
# def unpack_list(lst: list) -> tuple:
#     a, b, c = lst
#     return a, b, c
# ```

# **3. Tuple Packing**
# - Pack multiple variables into a single tuple.
# - Example: `def pack_into_tuple(a, b, c) -> tuple: ...`
# ```python
# def pack_into_tuple(a, b, c) -> tuple:
#     return a, b, c
# ```

# **4. List Packing**
# - Pack multiple variables into a single list.
# - Example: `def pack_into_list(a, b, c) -> list: ...`
# ```python
# def pack_into_list(a, b, c) -> list:
#     return [a, b, c]
# ```

# **5. Swapping Values Using Tuple Unpacking**
# - Swap two variables using tuple unpacking.
# - Example: `def swap_values(a, b) -> tuple: ...`
# ```python
# def swap_values(a, b) -> tuple:
#     a, b = b, a
#     return a, b
# ```

# **6. Unpacking with Ignoring Values**
# - Unpack a tuple but ignore some values.
# - Example: `def unpack_ignore(t: tuple) -> tuple: ...`
# ```python
# def unpack_ignore(t: tuple) -> tuple:
#     a, _, c = t
#     return a, c
# ```

# **7. Unpacking with Variable-Length Lists**
# - Unpack a list where the number of elements may vary.
# - Example: `def unpack_variable_length(lst: list) -> tuple: ...`
# ```python
# def unpack_variable_length(lst: list) -> tuple:
#     a, *rest = lst
#     return a, rest
# ```

# **8. Unpacking Dictionary Items**
# - Unpack dictionary items into key-value pairs.
# - Example: `def unpack_dict(d: dict) -> tuple: ...`
# ```python
# def unpack_dict(d: dict) -> tuple:
#     for key, value in d.items():
#         print(key, value)
# ```

# **9. Packing and Unpacking in Function Arguments**
# - Use `*args` and `**kwargs` to pack and unpack function arguments.
# - Example: `def func(a, *args, **kwargs): ...`
# ```python
# def func(a, *args, **kwargs):
#     return a, args, kwargs
# ```

# **10. Tuple Unpacking in Function Return**
# - Return multiple values from a function using a tuple and unpack them.
# - Example: `def return_multiple() -> tuple: ...`
# ```python
# def return_multiple() -> tuple:
#     return 1, 2, 3
# ```

# **11. List Unpacking in Function Return**
# - Return multiple values from a function using a list and unpack them.
# - Example: `def return_multiple_list() -> list: ...`
# ```python
# def return_multiple_list() -> list:
#     return [1, 2, 3]
# ```

# **12. Unpacking with Default Values**
# - Unpack a tuple with default values for missing items.
# - Example: `def unpack_with_defaults(t: tuple) -> tuple: ...`
# ```python
# def unpack_with_defaults(t: tuple) -> tuple:
#     a, b, c = (t + (None, None))[:3]
#     return a, b, c
# ```

# **13. Unpacking Nested Tuples**
# - Unpack values from nested tuples.
# - Example: `def unpack_nested_tuple(t: tuple) -> tuple: ...`
# ```python
# def unpack_nested_tuple(t: tuple) -> tuple:
#     (a, b), (c, d) = t
#     return a, b, c, d
# ```

# **14. Unpacking List of Tuples**
# - Unpack a list of tuples into separate lists.
# - Example: `def unpack_list_of_tuples(lst: list) -> tuple: ...`
# ```python
# def unpack_list_of_tuples(lst: list) -> tuple:
#     a, b = zip(*lst)
#     return list(a), list(b)
# ```

# **15. Unpacking with List Comprehension**
# - Use list comprehension to unpack values.
# - Example: `def unpack_with_comprehension(lst: list) -> list: ...`
# ```python
# def unpack_with_comprehension(lst: list) -> list:
#     return [x for x, _ in lst]
# ```

# **16. Unpacking Values with `*` Operator**
# - Unpack values from a list or tuple using the `*` operator.
# - Example: `def unpack_star(lst: list) -> tuple: ...`
# ```python
# def unpack_star(lst: list) -> tuple:
#     head, *tail = lst
#     return head, tail
# ```

# **17. Packing Values into a Dictionary**
# - Pack values into a dictionary using dictionary comprehension.
# - Example: `def pack_into_dict(keys: list, values: list) -> dict: ...`
# ```python
# def pack_into_dict(keys: list, values: list) -> dict:
#     return {k: v for k, v in zip(keys, values)}
# ```

# **18. Unpacking with `*` in Function Arguments**
# - Use `*` to unpack a list into function arguments.
# - Example: `def unpack_args(a, b, c): ...`
# ```python
# def unpack_args(a, b, c):
#     return a, b, c
#
# args = [1, 2, 3]
# unpack_args(*args)
# ```

# **19. Unpacking Nested Lists**
# - Unpack values from nested lists.
# - Example: `def unpack_nested_list(lst: list) -> tuple: ...`
# ```python
# def unpack_nested_list(lst: list) -> tuple:
#     [a, [b, c]] = lst
#     return a, b, c
# ```

# **20. Unpacking and Packing in List of Tuples**
# - Pack and unpack values from a list of tuples and use them in a function.
# - Example: `def process_tuples(lst: list) -> list: ...`
# ```python
# def process_tuples(lst: list) -> list:
#     return [a + b for (a, b) in lst]
# ```
