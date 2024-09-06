## function treated as object


def display():
    print("Hello world")


d = display

print(callable(d), callable(display), id(d), id(display))

d()


## nested function

def first_name(*, f, l):
    def last_name():
        return l

    print(f, last_name())


first_name(f="meet", l="kumar")


## function as parameter

def update_display(f):
    f()


update_display(display)


## function returning a function

def create_display():
    print("Outer function")

    def display_again():
        print("Hello world again")

    return display_again


hold_returning_func_ref = create_display()

hold_returning_func_ref()


## function closure (nested function)
def closure_func():
    msg = "local variable of closure function"
    print(msg)

    def nested():
        print("*" * 10)
        print(msg)
        print("*" * 10)

    return nested


cf = closure_func()
cf()


## caller class
class Dept:
    def __init__(self):
        self.depts = {
            "hr": "Human Resource",
            "f": "Finance",
            "it": "Information Technology",
            "acc": "Accounts",
            "mkt": "Marketing",
            "sd": "Sales and Distribution"
        }

    def __call__(self, *, dept):
        return self.depts[dept]


caller_class = Dept()
print(caller_class(dept="mkt"))


## convert caller class into closure function

def depts():
    departments = {
        "hr": "Human Resource",
        "f": "Finance",
        "it": "Information Technology",
        "acc": "Accounts",
        "mkt": "Marketing",
        "sd": "Sales and Distribution"
    }

    def dname(*, dept):
        return departments[dept]

    return dname


department = depts()
print(department(dept="it"))


## decorators
def decorator_func(func):
    print(111)

    def wrapper_func(da):
        print(222)
        func(da)
        print(333)

    return wrapper_func


@decorator_func
def display_func(data):
    print("Hello world!!!!!!!!! --->", data)


display_func("testing decorator")

## lambda function
km = lambda miles: miles * 1.6

print(km(10))

sum_of_three_nums = lambda a, *, b, c: a + b + c

print(sum_of_three_nums(10, b=20, c=30))

greater_between_two = lambda a, b: a if a > b else b

print(greater_between_two(10, 20))
