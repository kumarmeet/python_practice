<<<<<<< HEAD
## Nested Functions Templates:
# 1. Define a function with a nested function that returns the result of a calculation
def outer_function(x: int) -> int:
    def inner_function(y: int) -> int:
        return x + y

    return inner_function(5)


# 2. Define a function with a nested function that modifies an outer variable
def modify_outer_variable(x: int) -> int:
    def inner_function() -> int:
        nonlocal x
        x += 10
        return x

    return inner_function()


# 3. Define a function with a nested function that returns a string with both variables
def string_combination(x: str) -> str:
    def inner_function(y: str) -> str:
        return f"{x} {y}"

    return inner_function("World")


# 4. Define a function with a nested function that calculates the factorial of a number
def factorial(n: int) -> int:
    def inner_factorial(m: int) -> int:
        if m == 1:
            return 1
        else:
            return m * inner_factorial(m - 1)

    return inner_factorial(n)


# 5. Define a function with a nested function that demonstrates variable scope
def variable_scope() -> int:
    x = 5

    def inner_function() -> int:
        return x * 2

    return inner_function()


## Closures Templates:
# 1. Define a closure that remembers its outer variable value
def outer_function(x: int) -> callable:
    def inner_function(y: int) -> int:
        return x + y

    return inner_function


# 2. Define a closure that increments an outer variable
def incrementer(x: int) -> callable:
    def increment(y: int) -> int:
        nonlocal x
        x += y
        return x

    return increment


# 3. Define a closure that multiplies an outer variable
def multiplier(factor: int) -> callable:
    def multiply(x: int) -> int:
        return x * factor

    return multiply


# 4. Define a closure that generates a sequence of numbers
def sequence_generator(start: int) -> callable:
    def next_number(step: int) -> int:
        nonlocal start
        start += step
        return start

    return next_number


# 5. Define a closure that logs messages with a prefix
def logger(prefix: str) -> callable:
    def log(message: str) -> str:
        return f"{prefix}: {message}"

    return log


# 6. Define a closure that calculates the power of a base
def power(base: int) -> callable:
    def exponent(exp: int) -> int:
        return base ** exp

    return exponent


# 7. Define a closure that accumulates a running total
def accumulator() -> callable:
    total = 0

    def add(value: int) -> int:
        nonlocal total
        total += value
        return total

    return add


# 8. Define a closure that formats a number with a fixed precision
def precision_formatter(precision: int) -> callable:
    def format_number(number: float) -> str:
        return f"{number:.{precision}f}"

    return format_number


# 9. Define a closure that filters values based on a threshold
def threshold_filter(threshold: int) -> callable:
    def filter_value(value: int) -> bool:
        return value > threshold

    return filter_value


# 10. Define a closure that creates a custom greeting
def greeting_creator(greeting: str) -> callable:
    def greet(name: str) -> str:
        return f"{greeting}, {name}!"

    return greet


## Decorators Templates:
# 1. Define a decorator that prints the function name before calling it
def print_function_name(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        print(f"Function name: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


# 2. Define a decorator that measures the execution time of a function
import time


def timing_decorator(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result

    return wrapper


# 3. Define a decorator that logs the arguments of a function
def log_args(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        return func(*args, **kwargs)

    return wrapper


# 4. Define a decorator that enforces function argument types
def type_check(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        for (arg, expected_type) in zip(args, func.__annotations__.values()):
            if not isinstance(arg, expected_type):
                raise TypeError(f"Expected argument of type {expected_type}")
        return func(*args, **kwargs)

    return wrapper


# 5. Define a decorator that caches function results
def cache_results(func: callable) -> callable:
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


# 6. Define a decorator that checks if a function is called with a specific keyword argument
def check_keyword(keyword: str, value: any) -> callable:
    def decorator(func: callable) -> callable:
        def wrapper(*args, **kwargs):
            if kwargs.get(keyword) != value:
                raise ValueError(f"{keyword} must be {value}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


# 7. Define a decorator that modifies the return value of a function
def modify_return(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        return f"Modified: {return_value}"

    return wrapper


# 8. Define a decorator that limits the number of times a function can be called
def limit_calls(max_calls: int) -> callable:
    def decorator(func: callable) -> callable:
        calls = 0

        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls >= max_calls:
                raise RuntimeError("Function call limit exceeded")
            calls += 1
            return func(*args, **kwargs)

        return wrapper

    return decorator


# 9. Define a decorator that ensures a function is called with no arguments
def no_arguments(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        if args or kwargs:
            raise TypeError("This function does not accept any arguments")
        return func()

    return wrapper


# 10. Define a decorator that applies a transformation to the output of a function
def transform_output(transform: callable) -> callable:
    def decorator(func: callable) -> callable:
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return transform(result)

        return wrapper

    return decorator
=======
## Nested Functions Templates:
# 1. Define a function with a nested function that returns the result of a calculation
def outer_function(x: int) -> int:
    def inner_function(y: int) -> int:
        return x + y

    return inner_function(5)


# 2. Define a function with a nested function that modifies an outer variable
def modify_outer_variable(x: int) -> int:
    def inner_function() -> int:
        nonlocal x
        x += 10
        return x

    return inner_function()


# 3. Define a function with a nested function that returns a string with both variables
def string_combination(x: str) -> str:
    def inner_function(y: str) -> str:
        return f"{x} {y}"

    return inner_function("World")


# 4. Define a function with a nested function that calculates the factorial of a number
def factorial(n: int) -> int:
    def inner_factorial(m: int) -> int:
        if m == 1:
            return 1
        else:
            return m * inner_factorial(m - 1)

    return inner_factorial(n)


# 5. Define a function with a nested function that demonstrates variable scope
def variable_scope() -> int:
    x = 5

    def inner_function() -> int:
        return x * 2

    return inner_function()


## Closures Templates:
# 1. Define a closure that remembers its outer variable value
def outer_function(x: int) -> callable:
    def inner_function(y: int) -> int:
        return x + y

    return inner_function


# 2. Define a closure that increments an outer variable
def incrementer(x: int) -> callable:
    def increment(y: int) -> int:
        nonlocal x
        x += y
        return x

    return increment


# 3. Define a closure that multiplies an outer variable
def multiplier(factor: int) -> callable:
    def multiply(x: int) -> int:
        return x * factor

    return multiply


# 4. Define a closure that generates a sequence of numbers
def sequence_generator(start: int) -> callable:
    def next_number(step: int) -> int:
        nonlocal start
        start += step
        return start

    return next_number


# 5. Define a closure that logs messages with a prefix
def logger(prefix: str) -> callable:
    def log(message: str) -> str:
        return f"{prefix}: {message}"

    return log


# 6. Define a closure that calculates the power of a base
def power(base: int) -> callable:
    def exponent(exp: int) -> int:
        return base ** exp

    return exponent


# 7. Define a closure that accumulates a running total
def accumulator() -> callable:
    total = 0

    def add(value: int) -> int:
        nonlocal total
        total += value
        return total

    return add


# 8. Define a closure that formats a number with a fixed precision
def precision_formatter(precision: int) -> callable:
    def format_number(number: float) -> str:
        return f"{number:.{precision}f}"

    return format_number


# 9. Define a closure that filters values based on a threshold
def threshold_filter(threshold: int) -> callable:
    def filter_value(value: int) -> bool:
        return value > threshold

    return filter_value


# 10. Define a closure that creates a custom greeting
def greeting_creator(greeting: str) -> callable:
    def greet(name: str) -> str:
        return f"{greeting}, {name}!"

    return greet


## Decorators Templates:
# 1. Define a decorator that prints the function name before calling it
def print_function_name(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        print(f"Function name: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


# 2. Define a decorator that measures the execution time of a function
import time


def timing_decorator(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result

    return wrapper


# 3. Define a decorator that logs the arguments of a function
def log_args(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        return func(*args, **kwargs)

    return wrapper


# 4. Define a decorator that enforces function argument types
def type_check(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        for (arg, expected_type) in zip(args, func.__annotations__.values()):
            if not isinstance(arg, expected_type):
                raise TypeError(f"Expected argument of type {expected_type}")
        return func(*args, **kwargs)

    return wrapper


# 5. Define a decorator that caches function results
def cache_results(func: callable) -> callable:
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


# 6. Define a decorator that checks if a function is called with a specific keyword argument
def check_keyword(keyword: str, value: any) -> callable:
    def decorator(func: callable) -> callable:
        def wrapper(*args, **kwargs):
            if kwargs.get(keyword) != value:
                raise ValueError(f"{keyword} must be {value}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


# 7. Define a decorator that modifies the return value of a function
def modify_return(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        return f"Modified: {return_value}"

    return wrapper


# 8. Define a decorator that limits the number of times a function can be called
def limit_calls(max_calls: int) -> callable:
    def decorator(func: callable) -> callable:
        calls = 0

        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls >= max_calls:
                raise RuntimeError("Function call limit exceeded")
            calls += 1
            return func(*args, **kwargs)

        return wrapper

    return decorator


# 9. Define a decorator that ensures a function is called with no arguments
def no_arguments(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        if args or kwargs:
            raise TypeError("This function does not accept any arguments")
        return func()

    return wrapper


# 10. Define a decorator that applies a transformation to the output of a function
def transform_output(transform: callable) -> callable:
    def decorator(func: callable) -> callable:
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return transform(result)

        return wrapper

    return decorator
>>>>>>> 97ed5d77ef971ade0973f4b0714a4aeb250c0bf4
