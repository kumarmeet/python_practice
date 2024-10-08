<<<<<<< HEAD
# 1. String slicing
def extract_substring(s: str) -> str:
    # Return a substring using slicing
    return s[0:4]


# 2. String indexing
def access_negative_index(s: str) -> str:
    # Return the third character from the end using negative indexing
    return s[-3]


# 3. String concatenation
def concatenate_strings(str1: str, str2: str) -> str:
    # Concatenate two strings with a space between them
    return str1 + " " + str2


# 4. Uppercase conversion
def convert_to_uppercase(s: str) -> str:
    # Convert the string to uppercase
    return s.upper()


# 5. Lowercase conversion
def convert_to_lowercase(s: str) -> str:
    # Convert the string to lowercase
    return s.lower()


# 6. String immutability example
def explain_immutability() -> None:
    # Explain why strings are immutable
    pass


# 7. Checking string prefix
def starts_with_prefix(s: str, prefix: str) -> bool:
    # Check if the string starts with the given prefix
    return s.startswith(prefix)


# 8. String replacement
def replace_word(s: str, old_word: str, new_word: str) -> str:
    # Replace a word in the string
    return s.replace(old_word, new_word)


# 9. Splitting a string
def split_string(s: str, delimiter: str = ",") -> list[str]:
    # Split the string by the given delimiter
    return s.split(delimiter)


# 10. Joining a list of strings
def join_strings(words: list[str], delimiter: str = " ") -> str:
    # Join the list of words into a single string with a delimiter
    return delimiter.join(words)


# 11. Finding a substring
def find_substring(s: str, substring: str) -> int:
    # Find the first occurrence of the substring in the string
    return s.find(substring)


# 12. String trimming
def trim_string(s: str) -> str:
    # Remove leading and trailing whitespace from the string
    return s.strip()


# 13. Counting occurrences
def count_occurrences(s: str, char: str) -> int:
    # Count how many times a character appears in the string
    return s.count(char)


# 14. Checking for alphanumeric characters
def is_alphanumeric(s: str) -> bool:
    # Check if the string contains only alphanumeric characters
    return s.isalnum()


# 15. Checking for digits
def is_digit(s: str) -> bool:
    # Check if the string consists only of digits
    return s.isdigit()


# 16. String formatting (f-strings)
def format_string_f(name: str, age: int) -> str:
    # Format a string using f-strings
    return f"{name} {age}"


# 17. String formatting (.format method)
def format_string_format_method(num: int, item: str) -> str:
    # Format a string using the .format() method
    return "{}{}".format(num, item)


# 18. Checking for substring
def contains_substring(s: str, substring: str) -> bool:
    # Check if the substring exists in the string
    return True if substring in s else False


# 19. String reversal
def reverse_string(s: str) -> str:
    # Reverse the string
    return s[::-1]


# 20. Checking if string is lowercase
def is_lowercase(s: str) -> bool:
    # Check if the string is entirely lowercase
    return s.islower()


# 21. String capitalization
def capitalize_string(s: str) -> str:
    # Capitalize the first letter of the string
    return s.capitalize()


# 22. Finding last occurrence of substring
def find_last_occurrence(s: str, substring: str) -> int:
    # Return the index of the last occurrence of the substring
    return s.rfind(substring)


# 23. Checking startswith and endswith
def check_starts_and_ends(s: str, start: str, end: str) -> bool:
    # Check if the string starts with 'start' and ends with 'end'
    return s.startswith(start) and s.endswith(end)


# 24. String swapcase
def swap_case(s: str) -> str:
    # Swap the case of all characters in the string
    return s.swapcase()


# 25. String partition
def partition_string(s: str, separator: str) -> tuple[str, str, str]:
    # Split the string into three parts based on the separator
    return s.partition(separator)


# 26. Checking alphabetic and numeric
def is_alpha(s: str) -> bool:
    # Check if the string contains only alphabetic characters
    return s.isalpha()


def is_numeric(s: str) -> bool:
    # Check if the string contains only numeric characters
    return s.isnumeric()


# 27. String find vs index
def find_vs_index(s: str, substring: str) -> tuple[int, int]:
    # Find the position of the first occurrence using .find() and .index()
    return s.find(substring), s.index(substring)


# 28. Multiline string formatting
def multiline_string() -> str:
    # Return a formatted multiline string
    return """Hello world
    is the same
    data
    """


# 29. Counting occurrences of a word
def count_word_occurrences(s: str, word: str) -> int:
    # Count how many times a word appears in the string
    return s.count(word)


# 30. String zfill method
def pad_with_zeros(s: str, width: int) -> str:
    # Pad the string with zeros on the left to match the given width
    return s.zfill(width)
=======
# 1. String slicing
def extract_substring(s: str) -> str:
    # Return a substring using slicing
    return s[0:4]


# 2. String indexing
def access_negative_index(s: str) -> str:
    # Return the third character from the end using negative indexing
    return s[-3]


# 3. String concatenation
def concatenate_strings(str1: str, str2: str) -> str:
    # Concatenate two strings with a space between them
    return str1 + " " + str2


# 4. Uppercase conversion
def convert_to_uppercase(s: str) -> str:
    # Convert the string to uppercase
    return s.upper()


# 5. Lowercase conversion
def convert_to_lowercase(s: str) -> str:
    # Convert the string to lowercase
    return s.lower()


# 6. String immutability example
def explain_immutability() -> None:
    # Explain why strings are immutable
    pass


# 7. Checking string prefix
def starts_with_prefix(s: str, prefix: str) -> bool:
    # Check if the string starts with the given prefix
    return s.startswith(prefix)


# 8. String replacement
def replace_word(s: str, old_word: str, new_word: str) -> str:
    # Replace a word in the string
    return s.replace(old_word, new_word)


# 9. Splitting a string
def split_string(s: str, delimiter: str = ",") -> list[str]:
    # Split the string by the given delimiter
    return s.split(delimiter)


# 10. Joining a list of strings
def join_strings(words: list[str], delimiter: str = " ") -> str:
    # Join the list of words into a single string with a delimiter
    return delimiter.join(words)


# 11. Finding a substring
def find_substring(s: str, substring: str) -> int:
    # Find the first occurrence of the substring in the string
    return s.find(substring)


# 12. String trimming
def trim_string(s: str) -> str:
    # Remove leading and trailing whitespace from the string
    return s.strip()


# 13. Counting occurrences
def count_occurrences(s: str, char: str) -> int:
    # Count how many times a character appears in the string
    return s.count(char)


# 14. Checking for alphanumeric characters
def is_alphanumeric(s: str) -> bool:
    # Check if the string contains only alphanumeric characters
    return s.isalnum()


# 15. Checking for digits
def is_digit(s: str) -> bool:
    # Check if the string consists only of digits
    return s.isdigit()


# 16. String formatting (f-strings)
def format_string_f(name: str, age: int) -> str:
    # Format a string using f-strings
    return f"{name} {age}"


# 17. String formatting (.format method)
def format_string_format_method(num: int, item: str) -> str:
    # Format a string using the .format() method
    return "{}{}".format(num, item)


# 18. Checking for substring
def contains_substring(s: str, substring: str) -> bool:
    # Check if the substring exists in the string
    return True if substring in s else False


# 19. String reversal
def reverse_string(s: str) -> str:
    # Reverse the string
    return s[::-1]


# 20. Checking if string is lowercase
def is_lowercase(s: str) -> bool:
    # Check if the string is entirely lowercase
    return s.islower()


# 21. String capitalization
def capitalize_string(s: str) -> str:
    # Capitalize the first letter of the string
    return s.capitalize()


# 22. Finding last occurrence of substring
def find_last_occurrence(s: str, substring: str) -> int:
    # Return the index of the last occurrence of the substring
    return s.rfind(substring)


# 23. Checking startswith and endswith
def check_starts_and_ends(s: str, start: str, end: str) -> bool:
    # Check if the string starts with 'start' and ends with 'end'
    return s.startswith(start) and s.endswith(end)


# 24. String swapcase
def swap_case(s: str) -> str:
    # Swap the case of all characters in the string
    return s.swapcase()


# 25. String partition
def partition_string(s: str, separator: str) -> tuple[str, str, str]:
    # Split the string into three parts based on the separator
    return s.partition(separator)


# 26. Checking alphabetic and numeric
def is_alpha(s: str) -> bool:
    # Check if the string contains only alphabetic characters
    return s.isalpha()


def is_numeric(s: str) -> bool:
    # Check if the string contains only numeric characters
    return s.isnumeric()


# 27. String find vs index
def find_vs_index(s: str, substring: str) -> tuple[int, int]:
    # Find the position of the first occurrence using .find() and .index()
    return s.find(substring), s.index(substring)


# 28. Multiline string formatting
def multiline_string() -> str:
    # Return a formatted multiline string
    return """Hello world
    is the same
    data
    """


# 29. Counting occurrences of a word
def count_word_occurrences(s: str, word: str) -> int:
    # Count how many times a word appears in the string
    return s.count(word)


# 30. String zfill method
def pad_with_zeros(s: str, width: int) -> str:
    # Pad the string with zeros on the left to match the given width
    return s.zfill(width)
>>>>>>> 97ed5d77ef971ade0973f4b0714a4aeb250c0bf4
