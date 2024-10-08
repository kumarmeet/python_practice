<<<<<<< HEAD
# Python Syntax Practice Questions

# **1. Built-in Functions (Easy)**

# 1. **`len()`**
# - How do you use `len()` to get the number of elements in a list?
# - Example: `len([1, 2, 3])`

# 2. **`type()`**
# - How can you use `type()` to find the type of a variable?
# - Example: `type(42)`

# 3. **`id()`**
# - How do you get the unique identifier of an object using `id()`?
# - Example: `id('hello')`

# 4. **`abs()`**
# - How can `abs()` be used to find the absolute value of a number?
# - Example: `abs(-5)`

# 5. **`round()`**
# - How do you use `round()` to round a float to two decimal places?
# - Example: `round(3.14159, 2)`

# 6. **`sum()`**
# - How can `sum()` be used to get the total of a list of numbers?
# - Example: `sum([1, 2, 3, 4])`

# 7. **`min()`**
# - How do you use `min()` to find the smallest number in a list?
# - Example: `min([4, 2, 8])`

# 8. **`max()`**
# - How can `max()` be used to find the largest number in a list?
# - Example: `max([4, 2, 8])`

# 9. **`sorted()`**
# - How do you use `sorted()` to sort a list in ascending order?
# - Example: `sorted([3, 1, 2])`

# 10. **`reversed()`**
# - How can `reversed()` be used to reverse a list?
# - Example: `list(reversed([1, 2, 3]))`

# 11. **`enumerate()`**
# - How do you use `enumerate()` to get index-value pairs from a list?
# - Example: `list(enumerate(['a', 'b', 'c']))`

# 12. **`zip()`**
# - How can `zip()` be used to combine two lists into pairs?
# - Example: `list(zip([1, 2], ['a', 'b']))`

# 13. **`map()`**
# - How do you use `map()` to apply a function to each item in a list?
# - Example: `list(map(str, [1, 2, 3]))`

# 14. **`filter()`**
# - How can `filter()` be used to get even numbers from a list?
# - Example: `list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))`

# 15. **`range()`**
# - How do you use `range()` to generate a sequence of numbers?
# - Example: `list(range(5))`

# 16. **`list()`**
# - How can you convert a string to a list using `list()`?
# - Example: `list('hello')`

# 17. **`tuple()`**
# - How do you convert a list to a tuple using `tuple()`?
# - Example: `tuple([1, 2, 3])`

# 18. **`set()`**
# - How can `set()` be used to remove duplicates from a list?
# - Example: `set([1, 2, 2, 3])`

# 19. **`dict()`**
# - How do you create a dictionary from a list of tuples using `dict()`?
# - Example: `dict([(1, 'a'), (2, 'b')])`

# 20. **`str()`**
# - How can `str()` be used to convert an integer to a string?
# - Example: `str(123)`

# 21. **`int()`**
# - How do you convert a string to an integer using `int()`?
# - Example: `int('42')`

# 22. **`float()`**
# - How can `float()` be used to convert a string to a float?
# - Example: `float('3.14')`

# 23. **`bool()`**
# - How do you use `bool()` to convert a value to a boolean?
# - Example: `bool(0)`

# 24. **`chr()`**
# - How can `chr()` be used to get the character for an ASCII value?
# - Example: `chr(65)`

# 25. **`ord()`**
# - How do you get the ASCII value of a character using `ord()`?
# - Example: `ord('A')`

# **2. Strings (Easy)**

# 26. **`upper()`**
# - How do you convert a string to uppercase using `upper()`?
# - Example: `'hello'.upper()`

# 27. **`lower()`**
# - How can `lower()` be used to convert a string to lowercase?
# - Example: `'WORLD'.lower()`

# 28. **`strip()`**
# - How do you remove leading and trailing spaces from a string using `strip()`?
# - Example: `'  text  '.strip()`

# 29. **`replace()`**
# - How can `replace()` be used to replace a substring in a string?
# - Example: `'hello world'.replace('world', 'there')`

# 30. **`split()`**
# - How do you split a string into a list using `split()`?
# - Example: `'a,b,c'.split(',')`

# 31. **`join()`**
# - How can `join()` be used to concatenate a list of strings?
# - Example: `','.join(['a', 'b', 'c'])`

# 32. **`find()`**
# - How can you find the position of a substring in a string using `find()`?
# - Example: `'hello'.find('e')`

# 33. **`isdigit()`**
# - How can `isdigit()` be used to check if a string consists of digits?
# - Example: `'123'.isdigit()`

# 34. **`isalpha()`**
# - How do you use `isalpha()` to check if a string contains only alphabetic characters?
# - Example: `'abc'.isalpha()`

# 35. **`startswith()`**
# - How can `startswith()` be used to check if a string starts with a certain prefix?
# - Example: `'hello'.startswith('he')`

# 36. **`endswith()`**
# - How do you check if a string ends with a specific suffix using `endswith()`?
# - Example: `'hello'.endswith('lo')`

# **3. Lists (Easy)**

# 37. **Appending to a List**
# - How do you append an item to a list?
# - Example: `my_list.append(4)`

# 38. **Inserting into a List**
# - How can you insert an item at a specific position in a list?
# - Example: `my_list.insert(1, 'new')`

# 39. **Popping from a List**
# - How do you remove and return an item from a list using `pop()`?
# - Example: `my_list.pop()`

# 40. **List Slicing**
# - How do you slice a list to get a sublist?
# - Example: `my_list[1:3]`

# 41. **List Comprehension**
# - How can you create a list of squares from 1 to 5 using list comprehension?
# - Example: `[x**2 for x in range(1, 6)]`

# 42. **List Length**
# - How do you find the number of items in a list?
# - Example: `len(my_list)`

# 43. **List Sorting**
# - How can you sort a list in ascending order?
# - Example: `my_list.sort()`

# 44. **List Reversal**
# - How do you reverse a list in place?
# - Example: `my_list.reverse()`

# 45. **List Copy**
# - How can you create a copy of a list?
# - Example: `my_list.copy()`

# 46. **List Indexing**
# - How do you access the third item in a list?
# - Example: `my_list[2]`

# **4. Tuples (Easy)**

# 47. **Tuple Creation**
# - How do you create a tuple with three elements?
# - Example: `(1, 2, 3)`

# 48. **Accessing Tuple Elements**
# - How can you access the second element in a tuple?
# - Example: `my_tuple[1]`

# 49. **Tuple Unpacking**
# - How do you unpack a tuple into variables?
# - Example: `a, b, c = (1, 2, 3)`

# 50. **Tuple Length**
# - How can you find the number of items in a tuple?
# - Example: `len(my_tuple)`

# 51. **Tuple Indexing**
# - How do you find the index of a specific element in a tuple?
# - Example: `my_tuple.index(2)`

# 52. **Tuple Count**
# - How can `count()` be used to count occurrences of an element in a tuple?
# - Example: `my_tuple.count(1)`

# **5. Dictionaries (Easy)**

# 53. **Dictionary Creation**
# - How do you create a dictionary with keys and values?
# - Example: `my_dict = {'a': 1, 'b': 2}`

# 54. **Accessing Dictionary Values**
# - How can you access a value in a dictionary by key?
# - Example: `my_dict['a']`

# 55. **Adding to a Dictionary**
# - How do you add a new key-value pair to a dictionary?
# - Example: `my_dict['c'] = 3`

# 56. **Removing from a Dictionary**
# - How can you remove a key-value pair from a dictionary?
# - Example: `del my_dict['b']`

# 57. **Dictionary Keys**
# - How do you get all the keys from a dictionary?
# - Example: `my_dict.keys()`

# 58. **Dictionary Values**
# - How can you get all the values from a dictionary?
# - Example: `my_dict.values()`

# 59. **Dictionary Items**
# - How do you get all key-value pairs from a dictionary?
# - Example: `my_dict.items()`

# 60. **Dictionary Copy**
# - How can you create a copy of a dictionary?
# - Example: `my_dict.copy()`

# **6. Lists (Medium)**

# 61. **List Comprehension with Condition**
# - How can you use list comprehension to filter even numbers from 1 to 10?
# - Example: `[x for x in range(1, 11) if x % 2 == 0]`

# 62. **List Comprehension with Nested Loops**
# - How do you use list comprehension with nested loops to flatten a list of lists?
# - Example: `[item for sublist in [[1, 2], [3, 4]] for item in sublist]`

# 63. **List Comprehension with Functions**
# - How can you use list comprehension to apply a function to each item in a list?
# - Example: `[x**2 for x in [1, 2, 3]]`

# 64. **List Methods: `extend()`**
# - How do you use `extend()` to add elements from another list?
# - Example: `my_list.extend([4, 5])`

# 65. **List Methods: `remove()`**
# - How can you use `remove()` to delete a specific item from a list?
# - Example: `my_list.remove(3)`

# 66. **List Methods: `count()`**
# - How do you use `count()` to count occurrences of an element in a list?
# - Example: `my_list.count(1)`

# 67. **List Methods: `copy()`**
# - How can you use `copy()` to create a shallow copy of a list?
# - Example: `my_list.copy()`

# **7. Tuples (Medium)**

# 68. **Tuple Slicing**
# - How do you slice a tuple to get elements from index 1 to 3?
# - Example: `my_tuple[1:4]`

# 69. **Tuple Concatenation**
# - How can you concatenate two tuples?
# - Example: `(1, 2) + (3, 4)`

# 70. **Tuple Repetition**
# - How do you repeat a tuple multiple times?
# - Example: `(1, 2) * 3`

# 71. **Tuple Methods: `count()`**
# - How do you use `count()` to count occurrences of an element in a tuple?
# - Example: `my_tuple.count(1)`

# 72. **Tuple Methods: `index()`**
# - How can you find the index of an element in a tuple using `index()`?
# - Example: `my_tuple.index(2)`

# **8. Dictionaries (Medium)**

# 73. **Dictionary Comprehension**
# - How can you create a dictionary using dictionary comprehension?
# - Example: `{x: x**2 for x in range(5)}`

# 74. **Merging Dictionaries**
# - How do you merge two dictionaries?
# - Example: `{**dict1, **dict2}`

# 75. **Dictionary from Keys**
# - How can you create a dictionary with default values for all keys?
# - Example: `dict.fromkeys(['a', 'b'], 0)`

# 76. **Dictionary Method `popitem()`**
# - How do you use `popitem()` to remove and return an arbitrary key-value pair?
# - Example: `my_dict.popitem()`

# 77. **Dictionary Method `update()`**
# - How can `update()` be used to add key-value pairs from another dictionary?
# - Example: `my_dict.update({'c': 3})`

# 78. **Nested Dictionary Access**
# - How do you access a value in a nested dictionary?
# - Example: `my_dict['outer']['inner']`

# **9. Sets (Medium)**

# 79. **Set Operations: `union()`**
# - How can you use `union()` to combine two sets?
# - Example: `set1.union(set2)`

# 80. **Set Operations: `intersection()`**
# - How do you find the intersection of two sets using `intersection()`?
# - Example: `set1.intersection(set2)`

# 81. **Set Operations: `difference()`**
# - How can `difference()` be used to find elements in one set but not in another?
# - Example: `set1.difference(set2)`

# 82. **Set Operations: `symmetric_difference()`**
# - How do you use `symmetric_difference()` to find elements in either set but not both?
# - Example: `set1.symmetric_difference(set2)`

# 83. **Set Comprehension**
# - How can you create a set of squares from 1 to 5 using set comprehension?
# - Example: `{x**2 for x in range(1, 6)}`

# **10. Built-in Functions (Medium)**

# 84. **`callable()`**
# - How do you check if an object is callable using `callable()`?
# - Example: `callable(len)`

# 85. **`globals()`**
# - How can you access the global symbol table using `globals()`?
# - Example: `globals()`

# 86. **`locals()`**
# - How do you access the local symbol table using `locals()`?
# - Example: `locals()`

# 87. **`exec()`**
# - How can you execute a Python statement from a string using `exec()`?
# - Example: `exec('print("Hello World")')`

# 88. **`eval()`**
# - How do you evaluate a Python expression from a string using `eval()`?
# - Example: `eval('3 + 4')`

# 89. **`format()`**
# - How can you use `format()` to format a string with variables?
# - Example: `'{} {}'.format('Hello', 'World')`

# 90. **`hash()`**
# - How do you get the hash value of an object using `hash()`?
# - Example: `hash('example')`

# 91. **`divmod()`**
# - How can you use `divmod()` to get the quotient and remainder of a division?
# - Example: `divmod(7, 3)`

# 92. **`filter()` with Multiple Conditions**
# - How do you use `filter()` to apply multiple conditions to a list?
# - Example: `list(filter(lambda x: x > 0 and x < 10, [-1, 0, 5, 10]))`

# 93. **`map()` with Multiple Functions**
# - How can `map()` be used to apply multiple functions to a list?
# - Example: `list(map(lambda x: (x, x**2), [1, 2, 3]))`

# **11. Strings (Medium)**

# 94. **`format()` with Alignment**
# - How can you use `format()` to align text within a string?
# - Example: `'{} {:<10}'.format('Name:', 'John')`

# 95. **`zfill()`**
# - How do you use `zfill()` to pad a string with leading zeros?
# - Example: `'42'.zfill(5)`

# 96. **`rfind()`**
# - How can you use `rfind()` to find the last occurrence of a substring?
# - Example: `'hello world'.rfind('o')`

# 97. **`partition()`**
# - How do you split a string into three parts using `partition()`?
# - Example: `'hello world'.partition(' ')`

# 98. **`rjust()`**
# - How can `rjust()` be used to right-align a string with padding?
# - Example: `'42'.rjust(5, '0')`

# 99. **`rstrip()`**
# - How do you remove trailing characters from a string using `rstrip()`?
# - Example: `'text...'.rstrip('.')`

# 100. **`splitlines()`**
# - How can `splitlines()` be used to split a string into a list of lines?
# - Example: `'line1\nline2'.splitlines()`


# Python Syntax Practice Questions (Additional)

# **1. Built-in Functions (Easy)**

# 1. **`any()`**
# - How do you use `any()` to check if any item in a list is True?
# - Example: `any([False, True, False])`

# 2. **`all()`**
# - How can `all()` be used to check if all items in a list are True?
# - Example: `all([True, True, False])`

# 3. **`sum()` with Initial Value**
# - How do you use `sum()` to calculate the total with an initial value?
# - Example: `sum([1, 2, 3], 10)`

# 4. **`reversed()` with a List**
# - How can `reversed()` be used to reverse a list without changing the original list?
# - Example: `list(reversed([1, 2, 3]))`

# 5. **`list()` from a Range**
# - How do you use `list()` to create a list from a range of numbers?
# - Example: `list(range(5))`

# 6. **`dict()` with Key-Value Pairs**
# - How can you create a dictionary using keyword arguments?
# - Example: `dict(a=1, b=2)`

# 7. **`set()` from a List**
# - How do you convert a list to a set to remove duplicates?
# - Example: `set([1, 2, 2, 3])`

# 8. **`str()` with Formatting**
# - How can `str()` be used to format a number as a string with specific formatting?
# - Example: `str(123.456, '0.2f')`

# 9. **`float()` with Default Value**
# - How do you convert a value to float and handle exceptions if the conversion fails?
# - Example: `float('3.14')`

# 10. **`int()` with Base Conversion**
# - How can you use `int()` to convert a binary string to an integer?
# - Example: `int('1010', 2)`

# **2. Strings (Easy)**

# 11. **`capitalize()`**
# - How do you use `capitalize()` to capitalize the first letter of a string?
# - Example: `'hello'.capitalize()`

# 12. **`title()`**
# - How can `title()` be used to convert a string to title case?
# - Example: `'hello world'.title()`

# 13. **`center()`**
# - How do you use `center()` to center-align a string with padding?
# - Example: `'text'.center(10, '-')`

# 14. **`rfind()` with Start and End**
# - How can `rfind()` be used to find the last occurrence of a substring within a specific range?
# - Example: `'hello world'.rfind('o', 0, 5)`

# 15. **`lstrip()`**
# - How do you use `lstrip()` to remove leading characters from a string?
# - Example: `'   text'.lstrip()`

# 16. **`partition()` with Separator**
# - How can `partition()` be used to split a string at the first occurrence of a separator?
# - Example: `'a-b-c'.partition('-')`

# 17. **`swapcase()`**
# - How do you use `swapcase()` to swap the case of all characters in a string?
# - Example: `'Hello World'.swapcase()`

# 18. **`format()` with Positional and Keyword Arguments**
# - How can you use `format()` to include both positional and keyword arguments?
# - Example: `'{} {}'.format('Hello', 'World')`

# 19. **`translate()` with Translation Table**
# - How do you use `translate()` to replace characters based on a translation table?
# - Example: `'hello'.translate(str.maketrans('el', 'ip'))`

# 20. **`encode()`**
# - How can `encode()` be used to encode a string into bytes?
# - Example: `'text'.encode('utf-8')`

# **3. Lists (Medium)**

# 21. **`list()` with Tuple**
# - How do you use `list()` to convert a tuple into a list?
# - Example: `list((1, 2, 3))`

# 22. **`append()` vs `extend()`**
# - How do `append()` and `extend()` differ in adding elements to a list?
# - Example: `my_list.append([4, 5])` vs `my_list.extend([4, 5])`

# 23. **`remove()` with Error Handling**
# - How can you handle an error when removing an item from a list that may not exist?
# - Example: `try: my_list.remove(10) except ValueError: pass`

# 24. **`copy()` vs Slicing**
# - How do `copy()` and slicing compare for creating a shallow copy of a list?
# - Example: `my_list.copy()` vs `my_list[:]`

# 25. **`list()` with Generator Expression**
# - How can you convert a generator expression to a list?
# - Example: `list(x**2 for x in range(5))`

# 26. **List Methods: `clear()`**
# - How do you use `clear()` to remove all items from a list?
# - Example: `my_list.clear()`

# 27. **List Methods: `sort()` with Key**
# - How can you use `sort()` with a key function to sort a list?
# - Example: `my_list.sort(key=lambda x: len(x))`

# 28. **List Methods: `pop()` with Index**
# - How do you use `pop()` to remove an item at a specific index?
# - Example: `my_list.pop(2)`

# 29. **List Methods: `index()` with Start and End**
# - How can `index()` be used to find the position of an item within a specific range?
# - Example: `my_list.index(3, 0, 5)`

# 30. **List Methods: `reverse()`**
# - How do you reverse the order of items in a list in place?
# - Example: `my_list.reverse()`

# **4. Tuples (Medium)**

# 31. **Tuple Concatenation with Repeat**
# - How can you concatenate and repeat tuples?
# - Example: `(1, 2) + (3, 4) * 2`

# 32. **Tuple as Dictionary Key**
# - How can you use a tuple as a key in a dictionary?
# - Example: `my_dict = {('x', 'y'): 1}`

# 33. **Tuple Method: `count()` with Multiple Occurrences**
# - How do you use `count()` to find the number of occurrences of an element?
# - Example: `(1, 2, 2, 3).count(2)`

# 34. **Tuple Method: `index()` with Start and End**
# - How can you find the index of an element within a specific range in a tuple?
# - Example: `(1, 2, 3, 4).index(3, 0, 4)`

# **5. Dictionaries (Medium)**

# 35. **Dictionary Comprehension with Conditional**
# - How do you create a dictionary with a conditional expression in comprehension?
# - Example: `{x: x**2 for x in range(5) if x % 2 == 0}`

# 36. **Dictionary Methods: `pop()`**
# - How do you use `pop()` to remove a key-value pair and return the value?
# - Example: `my_dict.pop('key')`

# 37. **Dictionary Methods: `popitem()` with Error Handling**
# - How can you handle errors when using `popitem()` on an empty dictionary?
# - Example: `try: my_dict.popitem() except KeyError: pass`

# 38. **Dictionary Methods: `setdefault()`**
# - How do you use `setdefault()` to get a value or set a default if the key does not exist?
# - Example: `my_dict.setdefault('key', 0)`

# 39. **Dictionary Methods: `fromkeys()`**
# - How can `fromkeys()` be used to create a dictionary with a default value for all keys?
# - Example: `dict.fromkeys(['a', 'b'], 0)`

# **6. Sets (Medium)**

# 40. **Set Methods: `add()`**
# - How do you add an item to a set?
# - Example: `my_set.add(1)`

# 41. **Set Methods: `discard()`**
# - How can `discard()` be used to remove an item from a set without raising an error if it does not exist?
# - Example: `my_set.discard(1)`

# 42. **Set Methods: `pop()`**
# - How do you use `pop()` to remove and return an arbitrary item from a set?
# - Example: `my_set.pop()`

# 43. **Set Operations: `issubset()`**
# - How can `issubset()` be used to check if one set is a subset of another?
# - Example: `set1.issubset(set2)`

# 44. **Set Operations: `issuperset()`**
# - How do you use `issuperset()` to check if one set is a superset of another?
# - Example: `set1.issuperset(set2)`

# **7. Functions (Medium)**

# 45. **Function Annotations**
# - How can you add annotations to function parameters and return values?
# - Example: `def func(x: int) -> str:`

# 46. **Function with Default Values**
# - How do you define a function with default values for parameters?
# - Example: `def func(a, b=5):`

# 47. **Function Unpacking with `*args`**
# - How can `*args` be used to pass a variable number of arguments to a function?
# - Example: `def func(*args):`

# 48. **Function Unpacking with `**kwargs`**
# - How do you use `**kwargs` to pass a variable number of keyword arguments to a function?
# - Example: `def func(**kwargs):`

# 49. **Function as Argument**
# - How can you pass a function as an argument to another function?
# - Example: `def apply(func, x): return func(x)`

# 50. **Recursive Functions**
# - How do you define a recursive function to calculate factorial?
# - Example: `def factorial(n): return 1 if n == 0 else n * factorial(n-1)`

# Python Syntax Practice Questions (Additional)

# **1. Built-in Functions (Easy)**

# 1. **`chr()`**
# - How can you use `chr()` to get the character representation of an ASCII value?
# - Example: `chr(65)`

# 2. **`ord()`**
# - How do you use `ord()` to get the ASCII value of a character?
# - Example: `ord('A')`

# 3. **`dir()`**
# - How can `dir()` be used to list the attributes and methods of an object?
# - Example: `dir([])`

# 4. **`id()`**
# - How do you use `id()` to get the unique identifier of an object?
# - Example: `id([])`

# 5. **`eval()` with Expressions**
# - How can `eval()` be used to evaluate a mathematical expression from a string?
# - Example: `eval('2 + 3')`

# 6. **`callable()` with Custom Object**
# - How do you use `callable()` to check if a custom object is callable?
# - Example: `callable(lambda x: x)`

# 7. **`globals()` with Modification**
# - How can you use `globals()` to modify a global variable?
# - Example: `globals()['x'] = 10`

# 8. **`locals()` with Modification**
# - How do you use `locals()` to modify a local variable (though this is less common)?
# - Example: `locals()['x'] = 10`

# 9. **`hash()` with Immutable Types**
# - How can `hash()` be used to get the hash value of an immutable type?
# - Example: `hash('string')`

# 10. **`sorted()` with Key**
# - How do you use `sorted()` to sort a list with a custom key function?
# - Example: `sorted([('a', 2), ('b', 1)], key=lambda x: x[1])`

# **2. Strings (Medium)**

# 11. **`startswith()`**
# - How do you use `startswith()` to check if a string starts with a specific substring?
# - Example: `'hello'.startswith('he')`

# 12. **`endswith()`**
# - How can `endswith()` be used to check if a string ends with a specific substring?
# - Example: `'world'.endswith('ld')`

# 13. **`find()`**
# - How do you use `find()` to find the index of a substring, or return -1 if not found?
# - Example: `'hello'.find('lo')`

# 14. **`rjust()` with Padding Character**
# - How can you use `rjust()` to right-align a string with a custom padding character?
# - Example: `'42'.rjust(5, '0')`

# 15. **`ljust()`**
# - How do you use `ljust()` to left-align a string with padding?
# - Example: `'text'.ljust(10, '-')`

# 16. **`split()` with Maxsplit**
# - How can `split()` be used to split a string into a maximum number of parts?
# - Example: `'a,b,c,d'.split(',', 2)`

# 17. **`join()`**
# - How do you use `join()` to concatenate a list of strings into a single string?
# - Example: `'-'.join(['a', 'b', 'c'])`

# 18. **`strip()` with Characters**
# - How can `strip()` be used to remove specific characters from both ends of a string?
# - Example: `'--text--'.strip('-')`

# 19. **`casefold()`**
# - How do you use `casefold()` to perform a case-insensitive string comparison?
# - Example: `'HELLO'.casefold()`

# 20. **`removeprefix()`**
# - How can `removeprefix()` be used to remove a specified prefix from a string?
# - Example: `'TestHook'.removeprefix('Test')`

# **3. Lists (Medium)**

# 21. **`pop()` with Default**
# - How can you use `pop()` with a default value to handle cases where the list is empty?
# - Example: `my_list.pop(0, None)`

# 22. **`insert()`**
# - How do you use `insert()` to add an element at a specific index in a list?
# - Example: `my_list.insert(2, 'new')`

# 23. **`extend()` with Iterable**
# - How can `extend()` be used to add elements from any iterable to a list?
# - Example: `my_list.extend(set([1, 2]))`

# 24. **`list()` with Iterable**
# - How do you convert an iterable to a list using `list()`?
# - Example: `list(range(5))`

# 25. **List Comprehension with Multiple Conditions**
# - How can you use list comprehension to filter elements based on multiple conditions?
# - Example: `[x for x in range(10) if x % 2 == 0 if x > 5]`

# 26. **List Comprehension with Nested Conditions**
# - How do you create a list comprehension with nested conditions?
# - Example: `[x*y for x in range(2, 4) for y in range(2, 4)]`

# 27. **List Slicing with Step**
# - How can you slice a list with a step value?
# - Example: `my_list[::2]`

# 28. **List Methods: `insert()` with Index**
# - How do you use `insert()` to add an item at a specific index, considering edge cases?
# - Example: `my_list.insert(len(my_list), 'new')`

# 29. **List Methods: `copy()`**
# - How can `copy()` be used to create a shallow copy of a list?
# - Example: `my_list.copy()`

# 30. **List Methods: `index()` with Value Not Found**
# - How do you handle cases where `index()` might not find the item?
# - Example: `my_list.index('not_found')` (with error handling)

# **4. Tuples (Medium)**

# 31. **Tuple Unpacking**
# - How can you use tuple unpacking to assign values to multiple variables?
# - Example: `a, b, c = (1, 2, 3)`

# 32. **Tuple as Function Return**
# - How do you return multiple values from a function using a tuple?
# - Example: `def func(): return 1, 2`

# 33. **Tuple Methods: `count()` with Nested Tuples**
# - How do you use `count()` to count occurrences of a tuple within a tuple of tuples?
# - Example: `((1, 2), (1, 2)).count((1, 2))`

# 34. **Tuple Methods: `index()` with Nested Tuples**
# - How can you use `index()` to find the index of a nested tuple?
# - Example: `((1, 2), (3, 4)).index((3, 4))`

# **5. Dictionaries (Medium)**

# 35. **Dictionary Comprehension with Conditional and Iteration**
# - How can you use dictionary comprehension to create a dictionary with conditional logic and iteration?
# - Example: `{x: x**2 for x in range(10) if x % 2 == 0}`

# 36. **Dictionary Methods: `get()` with Default Value**
# - How do you use `get()` to retrieve a value with a default if the key does not exist?
# - Example: `my_dict.get('key', 'default')`

# 37. **Dictionary Methods: `update()` with Multiple Dictionaries**
# - How can `update()` be used to merge multiple dictionaries?
# - Example: `dict1.update(dict2, dict3)`

# 38. **Dictionary Methods: `keys()` with Iteration**
# - How do you iterate over dictionary keys using `keys()`?
# - Example: `for key in my_dict.keys():`

# 39. **Dictionary Methods: `values()` with Iteration**
# - How can you iterate over dictionary values using `values()`?
# - Example: `for value in my_dict.values():`

# **6. Sets (Medium)**

# 40. **Set Operations: `difference_update()`**
# - How do you use `difference_update()` to remove elements found in another set?
# - Example: `set1.difference_update(set2)`

# 41. **Set Operations: `intersection_update()`**
# - How can `intersection_update()` be used to keep only elements found in another set?
# - Example: `set1.intersection_update(set2)`

# 42. **Set Operations: `symmetric_difference_update()`**
# - How do you use `symmetric_difference_update()` to keep elements that are in either set but not both?
# - Example: `set1.symmetric_difference_update(set2)`

# 43. **Set Operations: `clear()`**
# - How can `clear()` be used to remove all elements from a set?
# - Example: `my_set.clear()`

# 44. **Set Operations: `union()` with Multiple Sets**
# - How do you use `union()` to combine multiple sets?
# - Example: `set1.union(set2, set3)`

# **7. Functions (Medium)**

# 45. **Function Default Arguments with Mutable Types**
# - How can you avoid issues when using mutable default arguments in a function?
# - Example: `def func(lst=[]):`

# 46. **Function with Arbitrary Keyword Arguments**
# - How do you handle arbitrary keyword arguments using `**kwargs`?
# - Example: `def func(**kwargs):`

# 47. **Function Decorators**
# - How can you apply a decorator to a function?
# - Example: `@decorator def func():`

# 48. **Lambda Functions with Multiple Arguments**
# - How do you define a lambda function that takes multiple arguments?
# - Example: `lambda x, y: x + y`

# 49. **Recursive Function with Base Case**
# - How do you implement a recursive function with a base case to prevent infinite recursion?
# - Example: `def factorial(n): return 1 if n == 0 else n * factorial(n - 1)`

# 50. **Generator Expressions with Yield**
# - How can you use a generator expression to create a generator function with `yield`?
# - Example: `def gen(): yield from range(5)`
=======
# Python Syntax Practice Questions

# **1. Built-in Functions (Easy)**

# 1. **`len()`**
# - How do you use `len()` to get the number of elements in a list?
# - Example: `len([1, 2, 3])`

# 2. **`type()`**
# - How can you use `type()` to find the type of a variable?
# - Example: `type(42)`

# 3. **`id()`**
# - How do you get the unique identifier of an object using `id()`?
# - Example: `id('hello')`

# 4. **`abs()`**
# - How can `abs()` be used to find the absolute value of a number?
# - Example: `abs(-5)`

# 5. **`round()`**
# - How do you use `round()` to round a float to two decimal places?
# - Example: `round(3.14159, 2)`

# 6. **`sum()`**
# - How can `sum()` be used to get the total of a list of numbers?
# - Example: `sum([1, 2, 3, 4])`

# 7. **`min()`**
# - How do you use `min()` to find the smallest number in a list?
# - Example: `min([4, 2, 8])`

# 8. **`max()`**
# - How can `max()` be used to find the largest number in a list?
# - Example: `max([4, 2, 8])`

# 9. **`sorted()`**
# - How do you use `sorted()` to sort a list in ascending order?
# - Example: `sorted([3, 1, 2])`

# 10. **`reversed()`**
# - How can `reversed()` be used to reverse a list?
# - Example: `list(reversed([1, 2, 3]))`

# 11. **`enumerate()`**
# - How do you use `enumerate()` to get index-value pairs from a list?
# - Example: `list(enumerate(['a', 'b', 'c']))`

# 12. **`zip()`**
# - How can `zip()` be used to combine two lists into pairs?
# - Example: `list(zip([1, 2], ['a', 'b']))`

# 13. **`map()`**
# - How do you use `map()` to apply a function to each item in a list?
# - Example: `list(map(str, [1, 2, 3]))`

# 14. **`filter()`**
# - How can `filter()` be used to get even numbers from a list?
# - Example: `list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))`

# 15. **`range()`**
# - How do you use `range()` to generate a sequence of numbers?
# - Example: `list(range(5))`

# 16. **`list()`**
# - How can you convert a string to a list using `list()`?
# - Example: `list('hello')`

# 17. **`tuple()`**
# - How do you convert a list to a tuple using `tuple()`?
# - Example: `tuple([1, 2, 3])`

# 18. **`set()`**
# - How can `set()` be used to remove duplicates from a list?
# - Example: `set([1, 2, 2, 3])`

# 19. **`dict()`**
# - How do you create a dictionary from a list of tuples using `dict()`?
# - Example: `dict([(1, 'a'), (2, 'b')])`

# 20. **`str()`**
# - How can `str()` be used to convert an integer to a string?
# - Example: `str(123)`

# 21. **`int()`**
# - How do you convert a string to an integer using `int()`?
# - Example: `int('42')`

# 22. **`float()`**
# - How can `float()` be used to convert a string to a float?
# - Example: `float('3.14')`

# 23. **`bool()`**
# - How do you use `bool()` to convert a value to a boolean?
# - Example: `bool(0)`

# 24. **`chr()`**
# - How can `chr()` be used to get the character for an ASCII value?
# - Example: `chr(65)`

# 25. **`ord()`**
# - How do you get the ASCII value of a character using `ord()`?
# - Example: `ord('A')`

# **2. Strings (Easy)**

# 26. **`upper()`**
# - How do you convert a string to uppercase using `upper()`?
# - Example: `'hello'.upper()`

# 27. **`lower()`**
# - How can `lower()` be used to convert a string to lowercase?
# - Example: `'WORLD'.lower()`

# 28. **`strip()`**
# - How do you remove leading and trailing spaces from a string using `strip()`?
# - Example: `'  text  '.strip()`

# 29. **`replace()`**
# - How can `replace()` be used to replace a substring in a string?
# - Example: `'hello world'.replace('world', 'there')`

# 30. **`split()`**
# - How do you split a string into a list using `split()`?
# - Example: `'a,b,c'.split(',')`

# 31. **`join()`**
# - How can `join()` be used to concatenate a list of strings?
# - Example: `','.join(['a', 'b', 'c'])`

# 32. **`find()`**
# - How can you find the position of a substring in a string using `find()`?
# - Example: `'hello'.find('e')`

# 33. **`isdigit()`**
# - How can `isdigit()` be used to check if a string consists of digits?
# - Example: `'123'.isdigit()`

# 34. **`isalpha()`**
# - How do you use `isalpha()` to check if a string contains only alphabetic characters?
# - Example: `'abc'.isalpha()`

# 35. **`startswith()`**
# - How can `startswith()` be used to check if a string starts with a certain prefix?
# - Example: `'hello'.startswith('he')`

# 36. **`endswith()`**
# - How do you check if a string ends with a specific suffix using `endswith()`?
# - Example: `'hello'.endswith('lo')`

# **3. Lists (Easy)**

# 37. **Appending to a List**
# - How do you append an item to a list?
# - Example: `my_list.append(4)`

# 38. **Inserting into a List**
# - How can you insert an item at a specific position in a list?
# - Example: `my_list.insert(1, 'new')`

# 39. **Popping from a List**
# - How do you remove and return an item from a list using `pop()`?
# - Example: `my_list.pop()`

# 40. **List Slicing**
# - How do you slice a list to get a sublist?
# - Example: `my_list[1:3]`

# 41. **List Comprehension**
# - How can you create a list of squares from 1 to 5 using list comprehension?
# - Example: `[x**2 for x in range(1, 6)]`

# 42. **List Length**
# - How do you find the number of items in a list?
# - Example: `len(my_list)`

# 43. **List Sorting**
# - How can you sort a list in ascending order?
# - Example: `my_list.sort()`

# 44. **List Reversal**
# - How do you reverse a list in place?
# - Example: `my_list.reverse()`

# 45. **List Copy**
# - How can you create a copy of a list?
# - Example: `my_list.copy()`

# 46. **List Indexing**
# - How do you access the third item in a list?
# - Example: `my_list[2]`

# **4. Tuples (Easy)**

# 47. **Tuple Creation**
# - How do you create a tuple with three elements?
# - Example: `(1, 2, 3)`

# 48. **Accessing Tuple Elements**
# - How can you access the second element in a tuple?
# - Example: `my_tuple[1]`

# 49. **Tuple Unpacking**
# - How do you unpack a tuple into variables?
# - Example: `a, b, c = (1, 2, 3)`

# 50. **Tuple Length**
# - How can you find the number of items in a tuple?
# - Example: `len(my_tuple)`

# 51. **Tuple Indexing**
# - How do you find the index of a specific element in a tuple?
# - Example: `my_tuple.index(2)`

# 52. **Tuple Count**
# - How can `count()` be used to count occurrences of an element in a tuple?
# - Example: `my_tuple.count(1)`

# **5. Dictionaries (Easy)**

# 53. **Dictionary Creation**
# - How do you create a dictionary with keys and values?
# - Example: `my_dict = {'a': 1, 'b': 2}`

# 54. **Accessing Dictionary Values**
# - How can you access a value in a dictionary by key?
# - Example: `my_dict['a']`

# 55. **Adding to a Dictionary**
# - How do you add a new key-value pair to a dictionary?
# - Example: `my_dict['c'] = 3`

# 56. **Removing from a Dictionary**
# - How can you remove a key-value pair from a dictionary?
# - Example: `del my_dict['b']`

# 57. **Dictionary Keys**
# - How do you get all the keys from a dictionary?
# - Example: `my_dict.keys()`

# 58. **Dictionary Values**
# - How can you get all the values from a dictionary?
# - Example: `my_dict.values()`

# 59. **Dictionary Items**
# - How do you get all key-value pairs from a dictionary?
# - Example: `my_dict.items()`

# 60. **Dictionary Copy**
# - How can you create a copy of a dictionary?
# - Example: `my_dict.copy()`

# **6. Lists (Medium)**

# 61. **List Comprehension with Condition**
# - How can you use list comprehension to filter even numbers from 1 to 10?
# - Example: `[x for x in range(1, 11) if x % 2 == 0]`

# 62. **List Comprehension with Nested Loops**
# - How do you use list comprehension with nested loops to flatten a list of lists?
# - Example: `[item for sublist in [[1, 2], [3, 4]] for item in sublist]`

# 63. **List Comprehension with Functions**
# - How can you use list comprehension to apply a function to each item in a list?
# - Example: `[x**2 for x in [1, 2, 3]]`

# 64. **List Methods: `extend()`**
# - How do you use `extend()` to add elements from another list?
# - Example: `my_list.extend([4, 5])`

# 65. **List Methods: `remove()`**
# - How can you use `remove()` to delete a specific item from a list?
# - Example: `my_list.remove(3)`

# 66. **List Methods: `count()`**
# - How do you use `count()` to count occurrences of an element in a list?
# - Example: `my_list.count(1)`

# 67. **List Methods: `copy()`**
# - How can you use `copy()` to create a shallow copy of a list?
# - Example: `my_list.copy()`

# **7. Tuples (Medium)**

# 68. **Tuple Slicing**
# - How do you slice a tuple to get elements from index 1 to 3?
# - Example: `my_tuple[1:4]`

# 69. **Tuple Concatenation**
# - How can you concatenate two tuples?
# - Example: `(1, 2) + (3, 4)`

# 70. **Tuple Repetition**
# - How do you repeat a tuple multiple times?
# - Example: `(1, 2) * 3`

# 71. **Tuple Methods: `count()`**
# - How do you use `count()` to count occurrences of an element in a tuple?
# - Example: `my_tuple.count(1)`

# 72. **Tuple Methods: `index()`**
# - How can you find the index of an element in a tuple using `index()`?
# - Example: `my_tuple.index(2)`

# **8. Dictionaries (Medium)**

# 73. **Dictionary Comprehension**
# - How can you create a dictionary using dictionary comprehension?
# - Example: `{x: x**2 for x in range(5)}`

# 74. **Merging Dictionaries**
# - How do you merge two dictionaries?
# - Example: `{**dict1, **dict2}`

# 75. **Dictionary from Keys**
# - How can you create a dictionary with default values for all keys?
# - Example: `dict.fromkeys(['a', 'b'], 0)`

# 76. **Dictionary Method `popitem()`**
# - How do you use `popitem()` to remove and return an arbitrary key-value pair?
# - Example: `my_dict.popitem()`

# 77. **Dictionary Method `update()`**
# - How can `update()` be used to add key-value pairs from another dictionary?
# - Example: `my_dict.update({'c': 3})`

# 78. **Nested Dictionary Access**
# - How do you access a value in a nested dictionary?
# - Example: `my_dict['outer']['inner']`

# **9. Sets (Medium)**

# 79. **Set Operations: `union()`**
# - How can you use `union()` to combine two sets?
# - Example: `set1.union(set2)`

# 80. **Set Operations: `intersection()`**
# - How do you find the intersection of two sets using `intersection()`?
# - Example: `set1.intersection(set2)`

# 81. **Set Operations: `difference()`**
# - How can `difference()` be used to find elements in one set but not in another?
# - Example: `set1.difference(set2)`

# 82. **Set Operations: `symmetric_difference()`**
# - How do you use `symmetric_difference()` to find elements in either set but not both?
# - Example: `set1.symmetric_difference(set2)`

# 83. **Set Comprehension**
# - How can you create a set of squares from 1 to 5 using set comprehension?
# - Example: `{x**2 for x in range(1, 6)}`

# **10. Built-in Functions (Medium)**

# 84. **`callable()`**
# - How do you check if an object is callable using `callable()`?
# - Example: `callable(len)`

# 85. **`globals()`**
# - How can you access the global symbol table using `globals()`?
# - Example: `globals()`

# 86. **`locals()`**
# - How do you access the local symbol table using `locals()`?
# - Example: `locals()`

# 87. **`exec()`**
# - How can you execute a Python statement from a string using `exec()`?
# - Example: `exec('print("Hello World")')`

# 88. **`eval()`**
# - How do you evaluate a Python expression from a string using `eval()`?
# - Example: `eval('3 + 4')`

# 89. **`format()`**
# - How can you use `format()` to format a string with variables?
# - Example: `'{} {}'.format('Hello', 'World')`

# 90. **`hash()`**
# - How do you get the hash value of an object using `hash()`?
# - Example: `hash('example')`

# 91. **`divmod()`**
# - How can you use `divmod()` to get the quotient and remainder of a division?
# - Example: `divmod(7, 3)`

# 92. **`filter()` with Multiple Conditions**
# - How do you use `filter()` to apply multiple conditions to a list?
# - Example: `list(filter(lambda x: x > 0 and x < 10, [-1, 0, 5, 10]))`

# 93. **`map()` with Multiple Functions**
# - How can `map()` be used to apply multiple functions to a list?
# - Example: `list(map(lambda x: (x, x**2), [1, 2, 3]))`

# **11. Strings (Medium)**

# 94. **`format()` with Alignment**
# - How can you use `format()` to align text within a string?
# - Example: `'{} {:<10}'.format('Name:', 'John')`

# 95. **`zfill()`**
# - How do you use `zfill()` to pad a string with leading zeros?
# - Example: `'42'.zfill(5)`

# 96. **`rfind()`**
# - How can you use `rfind()` to find the last occurrence of a substring?
# - Example: `'hello world'.rfind('o')`

# 97. **`partition()`**
# - How do you split a string into three parts using `partition()`?
# - Example: `'hello world'.partition(' ')`

# 98. **`rjust()`**
# - How can `rjust()` be used to right-align a string with padding?
# - Example: `'42'.rjust(5, '0')`

# 99. **`rstrip()`**
# - How do you remove trailing characters from a string using `rstrip()`?
# - Example: `'text...'.rstrip('.')`

# 100. **`splitlines()`**
# - How can `splitlines()` be used to split a string into a list of lines?
# - Example: `'line1\nline2'.splitlines()`


# Python Syntax Practice Questions (Additional)

# **1. Built-in Functions (Easy)**

# 1. **`any()`**
# - How do you use `any()` to check if any item in a list is True?
# - Example: `any([False, True, False])`

# 2. **`all()`**
# - How can `all()` be used to check if all items in a list are True?
# - Example: `all([True, True, False])`

# 3. **`sum()` with Initial Value**
# - How do you use `sum()` to calculate the total with an initial value?
# - Example: `sum([1, 2, 3], 10)`

# 4. **`reversed()` with a List**
# - How can `reversed()` be used to reverse a list without changing the original list?
# - Example: `list(reversed([1, 2, 3]))`

# 5. **`list()` from a Range**
# - How do you use `list()` to create a list from a range of numbers?
# - Example: `list(range(5))`

# 6. **`dict()` with Key-Value Pairs**
# - How can you create a dictionary using keyword arguments?
# - Example: `dict(a=1, b=2)`

# 7. **`set()` from a List**
# - How do you convert a list to a set to remove duplicates?
# - Example: `set([1, 2, 2, 3])`

# 8. **`str()` with Formatting**
# - How can `str()` be used to format a number as a string with specific formatting?
# - Example: `str(123.456, '0.2f')`

# 9. **`float()` with Default Value**
# - How do you convert a value to float and handle exceptions if the conversion fails?
# - Example: `float('3.14')`

# 10. **`int()` with Base Conversion**
# - How can you use `int()` to convert a binary string to an integer?
# - Example: `int('1010', 2)`

# **2. Strings (Easy)**

# 11. **`capitalize()`**
# - How do you use `capitalize()` to capitalize the first letter of a string?
# - Example: `'hello'.capitalize()`

# 12. **`title()`**
# - How can `title()` be used to convert a string to title case?
# - Example: `'hello world'.title()`

# 13. **`center()`**
# - How do you use `center()` to center-align a string with padding?
# - Example: `'text'.center(10, '-')`

# 14. **`rfind()` with Start and End**
# - How can `rfind()` be used to find the last occurrence of a substring within a specific range?
# - Example: `'hello world'.rfind('o', 0, 5)`

# 15. **`lstrip()`**
# - How do you use `lstrip()` to remove leading characters from a string?
# - Example: `'   text'.lstrip()`

# 16. **`partition()` with Separator**
# - How can `partition()` be used to split a string at the first occurrence of a separator?
# - Example: `'a-b-c'.partition('-')`

# 17. **`swapcase()`**
# - How do you use `swapcase()` to swap the case of all characters in a string?
# - Example: `'Hello World'.swapcase()`

# 18. **`format()` with Positional and Keyword Arguments**
# - How can you use `format()` to include both positional and keyword arguments?
# - Example: `'{} {}'.format('Hello', 'World')`

# 19. **`translate()` with Translation Table**
# - How do you use `translate()` to replace characters based on a translation table?
# - Example: `'hello'.translate(str.maketrans('el', 'ip'))`

# 20. **`encode()`**
# - How can `encode()` be used to encode a string into bytes?
# - Example: `'text'.encode('utf-8')`

# **3. Lists (Medium)**

# 21. **`list()` with Tuple**
# - How do you use `list()` to convert a tuple into a list?
# - Example: `list((1, 2, 3))`

# 22. **`append()` vs `extend()`**
# - How do `append()` and `extend()` differ in adding elements to a list?
# - Example: `my_list.append([4, 5])` vs `my_list.extend([4, 5])`

# 23. **`remove()` with Error Handling**
# - How can you handle an error when removing an item from a list that may not exist?
# - Example: `try: my_list.remove(10) except ValueError: pass`

# 24. **`copy()` vs Slicing**
# - How do `copy()` and slicing compare for creating a shallow copy of a list?
# - Example: `my_list.copy()` vs `my_list[:]`

# 25. **`list()` with Generator Expression**
# - How can you convert a generator expression to a list?
# - Example: `list(x**2 for x in range(5))`

# 26. **List Methods: `clear()`**
# - How do you use `clear()` to remove all items from a list?
# - Example: `my_list.clear()`

# 27. **List Methods: `sort()` with Key**
# - How can you use `sort()` with a key function to sort a list?
# - Example: `my_list.sort(key=lambda x: len(x))`

# 28. **List Methods: `pop()` with Index**
# - How do you use `pop()` to remove an item at a specific index?
# - Example: `my_list.pop(2)`

# 29. **List Methods: `index()` with Start and End**
# - How can `index()` be used to find the position of an item within a specific range?
# - Example: `my_list.index(3, 0, 5)`

# 30. **List Methods: `reverse()`**
# - How do you reverse the order of items in a list in place?
# - Example: `my_list.reverse()`

# **4. Tuples (Medium)**

# 31. **Tuple Concatenation with Repeat**
# - How can you concatenate and repeat tuples?
# - Example: `(1, 2) + (3, 4) * 2`

# 32. **Tuple as Dictionary Key**
# - How can you use a tuple as a key in a dictionary?
# - Example: `my_dict = {('x', 'y'): 1}`

# 33. **Tuple Method: `count()` with Multiple Occurrences**
# - How do you use `count()` to find the number of occurrences of an element?
# - Example: `(1, 2, 2, 3).count(2)`

# 34. **Tuple Method: `index()` with Start and End**
# - How can you find the index of an element within a specific range in a tuple?
# - Example: `(1, 2, 3, 4).index(3, 0, 4)`

# **5. Dictionaries (Medium)**

# 35. **Dictionary Comprehension with Conditional**
# - How do you create a dictionary with a conditional expression in comprehension?
# - Example: `{x: x**2 for x in range(5) if x % 2 == 0}`

# 36. **Dictionary Methods: `pop()`**
# - How do you use `pop()` to remove a key-value pair and return the value?
# - Example: `my_dict.pop('key')`

# 37. **Dictionary Methods: `popitem()` with Error Handling**
# - How can you handle errors when using `popitem()` on an empty dictionary?
# - Example: `try: my_dict.popitem() except KeyError: pass`

# 38. **Dictionary Methods: `setdefault()`**
# - How do you use `setdefault()` to get a value or set a default if the key does not exist?
# - Example: `my_dict.setdefault('key', 0)`

# 39. **Dictionary Methods: `fromkeys()`**
# - How can `fromkeys()` be used to create a dictionary with a default value for all keys?
# - Example: `dict.fromkeys(['a', 'b'], 0)`

# **6. Sets (Medium)**

# 40. **Set Methods: `add()`**
# - How do you add an item to a set?
# - Example: `my_set.add(1)`

# 41. **Set Methods: `discard()`**
# - How can `discard()` be used to remove an item from a set without raising an error if it does not exist?
# - Example: `my_set.discard(1)`

# 42. **Set Methods: `pop()`**
# - How do you use `pop()` to remove and return an arbitrary item from a set?
# - Example: `my_set.pop()`

# 43. **Set Operations: `issubset()`**
# - How can `issubset()` be used to check if one set is a subset of another?
# - Example: `set1.issubset(set2)`

# 44. **Set Operations: `issuperset()`**
# - How do you use `issuperset()` to check if one set is a superset of another?
# - Example: `set1.issuperset(set2)`

# **7. Functions (Medium)**

# 45. **Function Annotations**
# - How can you add annotations to function parameters and return values?
# - Example: `def func(x: int) -> str:`

# 46. **Function with Default Values**
# - How do you define a function with default values for parameters?
# - Example: `def func(a, b=5):`

# 47. **Function Unpacking with `*args`**
# - How can `*args` be used to pass a variable number of arguments to a function?
# - Example: `def func(*args):`

# 48. **Function Unpacking with `**kwargs`**
# - How do you use `**kwargs` to pass a variable number of keyword arguments to a function?
# - Example: `def func(**kwargs):`

# 49. **Function as Argument**
# - How can you pass a function as an argument to another function?
# - Example: `def apply(func, x): return func(x)`

# 50. **Recursive Functions**
# - How do you define a recursive function to calculate factorial?
# - Example: `def factorial(n): return 1 if n == 0 else n * factorial(n-1)`

# Python Syntax Practice Questions (Additional)

# **1. Built-in Functions (Easy)**

# 1. **`chr()`**
# - How can you use `chr()` to get the character representation of an ASCII value?
# - Example: `chr(65)`

# 2. **`ord()`**
# - How do you use `ord()` to get the ASCII value of a character?
# - Example: `ord('A')`

# 3. **`dir()`**
# - How can `dir()` be used to list the attributes and methods of an object?
# - Example: `dir([])`

# 4. **`id()`**
# - How do you use `id()` to get the unique identifier of an object?
# - Example: `id([])`

# 5. **`eval()` with Expressions**
# - How can `eval()` be used to evaluate a mathematical expression from a string?
# - Example: `eval('2 + 3')`

# 6. **`callable()` with Custom Object**
# - How do you use `callable()` to check if a custom object is callable?
# - Example: `callable(lambda x: x)`

# 7. **`globals()` with Modification**
# - How can you use `globals()` to modify a global variable?
# - Example: `globals()['x'] = 10`

# 8. **`locals()` with Modification**
# - How do you use `locals()` to modify a local variable (though this is less common)?
# - Example: `locals()['x'] = 10`

# 9. **`hash()` with Immutable Types**
# - How can `hash()` be used to get the hash value of an immutable type?
# - Example: `hash('string')`

# 10. **`sorted()` with Key**
# - How do you use `sorted()` to sort a list with a custom key function?
# - Example: `sorted([('a', 2), ('b', 1)], key=lambda x: x[1])`

# **2. Strings (Medium)**

# 11. **`startswith()`**
# - How do you use `startswith()` to check if a string starts with a specific substring?
# - Example: `'hello'.startswith('he')`

# 12. **`endswith()`**
# - How can `endswith()` be used to check if a string ends with a specific substring?
# - Example: `'world'.endswith('ld')`

# 13. **`find()`**
# - How do you use `find()` to find the index of a substring, or return -1 if not found?
# - Example: `'hello'.find('lo')`

# 14. **`rjust()` with Padding Character**
# - How can you use `rjust()` to right-align a string with a custom padding character?
# - Example: `'42'.rjust(5, '0')`

# 15. **`ljust()`**
# - How do you use `ljust()` to left-align a string with padding?
# - Example: `'text'.ljust(10, '-')`

# 16. **`split()` with Maxsplit**
# - How can `split()` be used to split a string into a maximum number of parts?
# - Example: `'a,b,c,d'.split(',', 2)`

# 17. **`join()`**
# - How do you use `join()` to concatenate a list of strings into a single string?
# - Example: `'-'.join(['a', 'b', 'c'])`

# 18. **`strip()` with Characters**
# - How can `strip()` be used to remove specific characters from both ends of a string?
# - Example: `'--text--'.strip('-')`

# 19. **`casefold()`**
# - How do you use `casefold()` to perform a case-insensitive string comparison?
# - Example: `'HELLO'.casefold()`

# 20. **`removeprefix()`**
# - How can `removeprefix()` be used to remove a specified prefix from a string?
# - Example: `'TestHook'.removeprefix('Test')`

# **3. Lists (Medium)**

# 21. **`pop()` with Default**
# - How can you use `pop()` with a default value to handle cases where the list is empty?
# - Example: `my_list.pop(0, None)`

# 22. **`insert()`**
# - How do you use `insert()` to add an element at a specific index in a list?
# - Example: `my_list.insert(2, 'new')`

# 23. **`extend()` with Iterable**
# - How can `extend()` be used to add elements from any iterable to a list?
# - Example: `my_list.extend(set([1, 2]))`

# 24. **`list()` with Iterable**
# - How do you convert an iterable to a list using `list()`?
# - Example: `list(range(5))`

# 25. **List Comprehension with Multiple Conditions**
# - How can you use list comprehension to filter elements based on multiple conditions?
# - Example: `[x for x in range(10) if x % 2 == 0 if x > 5]`

# 26. **List Comprehension with Nested Conditions**
# - How do you create a list comprehension with nested conditions?
# - Example: `[x*y for x in range(2, 4) for y in range(2, 4)]`

# 27. **List Slicing with Step**
# - How can you slice a list with a step value?
# - Example: `my_list[::2]`

# 28. **List Methods: `insert()` with Index**
# - How do you use `insert()` to add an item at a specific index, considering edge cases?
# - Example: `my_list.insert(len(my_list), 'new')`

# 29. **List Methods: `copy()`**
# - How can `copy()` be used to create a shallow copy of a list?
# - Example: `my_list.copy()`

# 30. **List Methods: `index()` with Value Not Found**
# - How do you handle cases where `index()` might not find the item?
# - Example: `my_list.index('not_found')` (with error handling)

# **4. Tuples (Medium)**

# 31. **Tuple Unpacking**
# - How can you use tuple unpacking to assign values to multiple variables?
# - Example: `a, b, c = (1, 2, 3)`

# 32. **Tuple as Function Return**
# - How do you return multiple values from a function using a tuple?
# - Example: `def func(): return 1, 2`

# 33. **Tuple Methods: `count()` with Nested Tuples**
# - How do you use `count()` to count occurrences of a tuple within a tuple of tuples?
# - Example: `((1, 2), (1, 2)).count((1, 2))`

# 34. **Tuple Methods: `index()` with Nested Tuples**
# - How can you use `index()` to find the index of a nested tuple?
# - Example: `((1, 2), (3, 4)).index((3, 4))`

# **5. Dictionaries (Medium)**

# 35. **Dictionary Comprehension with Conditional and Iteration**
# - How can you use dictionary comprehension to create a dictionary with conditional logic and iteration?
# - Example: `{x: x**2 for x in range(10) if x % 2 == 0}`

# 36. **Dictionary Methods: `get()` with Default Value**
# - How do you use `get()` to retrieve a value with a default if the key does not exist?
# - Example: `my_dict.get('key', 'default')`

# 37. **Dictionary Methods: `update()` with Multiple Dictionaries**
# - How can `update()` be used to merge multiple dictionaries?
# - Example: `dict1.update(dict2, dict3)`

# 38. **Dictionary Methods: `keys()` with Iteration**
# - How do you iterate over dictionary keys using `keys()`?
# - Example: `for key in my_dict.keys():`

# 39. **Dictionary Methods: `values()` with Iteration**
# - How can you iterate over dictionary values using `values()`?
# - Example: `for value in my_dict.values():`

# **6. Sets (Medium)**

# 40. **Set Operations: `difference_update()`**
# - How do you use `difference_update()` to remove elements found in another set?
# - Example: `set1.difference_update(set2)`

# 41. **Set Operations: `intersection_update()`**
# - How can `intersection_update()` be used to keep only elements found in another set?
# - Example: `set1.intersection_update(set2)`

# 42. **Set Operations: `symmetric_difference_update()`**
# - How do you use `symmetric_difference_update()` to keep elements that are in either set but not both?
# - Example: `set1.symmetric_difference_update(set2)`

# 43. **Set Operations: `clear()`**
# - How can `clear()` be used to remove all elements from a set?
# - Example: `my_set.clear()`

# 44. **Set Operations: `union()` with Multiple Sets**
# - How do you use `union()` to combine multiple sets?
# - Example: `set1.union(set2, set3)`

# **7. Functions (Medium)**

# 45. **Function Default Arguments with Mutable Types**
# - How can you avoid issues when using mutable default arguments in a function?
# - Example: `def func(lst=[]):`

# 46. **Function with Arbitrary Keyword Arguments**
# - How do you handle arbitrary keyword arguments using `**kwargs`?
# - Example: `def func(**kwargs):`

# 47. **Function Decorators**
# - How can you apply a decorator to a function?
# - Example: `@decorator def func():`

# 48. **Lambda Functions with Multiple Arguments**
# - How do you define a lambda function that takes multiple arguments?
# - Example: `lambda x, y: x + y`

# 49. **Recursive Function with Base Case**
# - How do you implement a recursive function with a base case to prevent infinite recursion?
# - Example: `def factorial(n): return 1 if n == 0 else n * factorial(n - 1)`

# 50. **Generator Expressions with Yield**
# - How can you use a generator expression to create a generator function with `yield`?
# - Example: `def gen(): yield from range(5)`
>>>>>>> 97ed5d77ef971ade0973f4b0714a4aeb250c0bf4
