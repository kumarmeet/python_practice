<<<<<<< HEAD
# 1. Define a lambda function that adds two numbers
add = lambda x, y: x + y

# 2. Define a lambda function that returns the square of a number
square = lambda x: x ** 2

# 3. Define a lambda function that returns the maximum of two numbers
maximum = lambda x, y: x if x > y else y

# 4. Define a lambda function that checks if a number is even
is_even = lambda x: x % 2 == 0

# 5. Define a lambda function that returns the length of a string
string_length = lambda s: len(s)

# 6. Define a lambda function that concatenates two strings
concat_strings = lambda s1, s2: s1 + s2

# 7. Define a lambda function that returns the factorial of a number
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

# 8. Define a lambda function that returns a list of squares from 1 to n
squares_list = lambda n: [i ** 2 for i in range(1, n + 1)]

# 9. Define a lambda function that returns True if a string contains a vowel
contains_vowel = lambda s: any(v in s for v in 'aeiou')

# 10. Define a lambda function that applies a function to a list of numbers
apply_function = lambda func, lst: [func(x) for x in lst]

# 11. Define a lambda function that returns the sum of all elements in a list
sum_list = lambda lst: sum(lst)

# 12. Define a lambda function that returns a list of tuples with elements from two lists
zip_lists = lambda lst1, lst2: list(zip(lst1, lst2))

# 13. Define a lambda function that sorts a list of strings by their length
sort_by_length = lambda lst: sorted(lst, key=lambda s: len(s))

# 14. Define a lambda function that filters out odd numbers from a list
filter_odds = lambda lst: [x for x in lst if x % 2 == 0]

# 15. Define a lambda function that returns the reversed version of a string
reverse_string = lambda s: s[::-1]

# 16. Define a lambda function that raises a number to the power of another number
power = lambda x, y: x ** y

# 17. Define a lambda function that converts a temperature from Celsius to Fahrenheit
c_to_f = lambda c: (c * 9 / 5) + 32

# 18. Define a lambda function that calculates the average of a list of numbers
average = lambda lst: sum(lst) / len(lst) if lst else 0

# 19. Define a lambda function that returns a dictionary with keys as list elements and values as their squares
dict_squares = lambda lst: {x: x ** 2 for x in lst}

# 20. Define a lambda function that returns the product of all numbers in a list
product_list = lambda lst: 1 if not lst else lst[0] * product_list(lst[1:])
=======
# 1. Define a lambda function that adds two numbers
add = lambda x, y: x + y

# 2. Define a lambda function that returns the square of a number
square = lambda x: x ** 2

# 3. Define a lambda function that returns the maximum of two numbers
maximum = lambda x, y: x if x > y else y

# 4. Define a lambda function that checks if a number is even
is_even = lambda x: x % 2 == 0

# 5. Define a lambda function that returns the length of a string
string_length = lambda s: len(s)

# 6. Define a lambda function that concatenates two strings
concat_strings = lambda s1, s2: s1 + s2

# 7. Define a lambda function that returns the factorial of a number
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

# 8. Define a lambda function that returns a list of squares from 1 to n
squares_list = lambda n: [i ** 2 for i in range(1, n + 1)]

# 9. Define a lambda function that returns True if a string contains a vowel
contains_vowel = lambda s: any(v in s for v in 'aeiou')

# 10. Define a lambda function that applies a function to a list of numbers
apply_function = lambda func, lst: [func(x) for x in lst]

# 11. Define a lambda function that returns the sum of all elements in a list
sum_list = lambda lst: sum(lst)

# 12. Define a lambda function that returns a list of tuples with elements from two lists
zip_lists = lambda lst1, lst2: list(zip(lst1, lst2))

# 13. Define a lambda function that sorts a list of strings by their length
sort_by_length = lambda lst: sorted(lst, key=lambda s: len(s))

# 14. Define a lambda function that filters out odd numbers from a list
filter_odds = lambda lst: [x for x in lst if x % 2 == 0]

# 15. Define a lambda function that returns the reversed version of a string
reverse_string = lambda s: s[::-1]

# 16. Define a lambda function that raises a number to the power of another number
power = lambda x, y: x ** y

# 17. Define a lambda function that converts a temperature from Celsius to Fahrenheit
c_to_f = lambda c: (c * 9 / 5) + 32

# 18. Define a lambda function that calculates the average of a list of numbers
average = lambda lst: sum(lst) / len(lst) if lst else 0

# 19. Define a lambda function that returns a dictionary with keys as list elements and values as their squares
dict_squares = lambda lst: {x: x ** 2 for x in lst}

# 20. Define a lambda function that returns the product of all numbers in a list
product_list = lambda lst: 1 if not lst else lst[0] * product_list(lst[1:])
>>>>>>> 97ed5d77ef971ade0973f4b0714a4aeb250c0bf4
