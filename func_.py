## always share same reference of call by reference


def call_by_reference(a, b, c):
    a = 55  ## creates new local reference due to int is immutable
    print("Inside of function", id(a), id(b), id(c))


x, y, z = 10, 12, 14

print("Outside of function", id(x), id(y), id(z))
call_by_reference(x, y, z)


## positional vs keyword args
def net_sal(basic, allowance, deduction):
    print("basic", basic)
    print("allowance", allowance)
    print("deduction", deduction)
    net = basic + allowance - deduction
    return net


result = net_sal(allowance=2000, basic=4000, deduction=1000)

print(result)


## default args

def default_args(a, b, c=44):
    print(a, b, c)


## default create only once

def default_once(item, l=[]):
    l.append(item)
    return l


default_args(10, 20)
default_args(10, 20, 55)

default_once(10)
default_once(10)
default_once(10)

print(default_once(20))


## only positional or only keywords args

## mixed positional or keywords
def example_one(a, b, c, d, e, f):
    print(a, b, c, d, e, f)


example_one(1, 2, c=4, d=8, e=1, f=1)
example_one(1, 1, 1, 1, 1, 1)


## before / must be positional after / can be positional or keyword args
def example_two(a, b, /, c, d, e, f):
    print(a, b, c, d, e, f)


example_two(10, 20, c=1, d=3, e=4, f=4)
example_two(10, 20, 10, 20, 30, 40)


## before * can be positional or keywords after * must be keyword args

def example_three(a, b, /, c, *, d, e, f):
    print(a, b, c, d, e, f)


example_three(10, 20, c=20, d=15, e=65, f=99)


## variable length, unpacking and multiple arguments

## variable length
## before variable args must be positional and after must be keyword args
def fun1(a, b, *args):
    print(a, b, args, type(args))


fun1(1, 2, 3, 4, 5, 6)
fun1("hello", "data")

l1 = [10, 20, 30, 40, 50, 60]


## unpacking
def fun2(a, b, *c):
    print(a, b, c)


fun2(*l1)
fun2(5, 6, 7, 8, 9, 10, 55)


## multiple return
def fun3(e, f, g):
    return e + 1, f + 2, g + 3


a, b, c = fun3(10, 20, 30)

res = fun3(30, 40, 50)

print(a, b, c, res, type(res))


## variations of keyword variable length args
def fun4(**kwargs):
    print(kwargs, type(kwargs))


fun4(name="meet kumar", age=34)


def fun5(i, j, *args, **kwargs):
    print(i, j, args, kwargs)


fun5(10, 20, 5, 6, 9, 8, 7, 5, uid=101, role=["admin", "user"])

## iterators and generators
l2 = [1, 2, 3, 4, 5, 6]

itr = iter(l2)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))


def days():
    l = ["sun", "mon", "tue", "wed", "thur", "fri", "sat"]

    i = 0
    while True:
        print("yield", i)
        p = l[i]
        i = (i + 1) % 7
        yield p


it = days()

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

## global variable variable not changed by default
g = 15


def glob_var():
    global g  ## want to modified then use global keyword in func
    g = g + 10
    m = 12  ## local variable
    print(g, m)


glob_var()


## globals and locals functions

def locals_data(w=10, q=20):
    k, r, u = 20, 30, 440
    print(locals(), type(locals()))


locals_data()

print(globals().keys())


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


factorial = fact(5)
print(factorial)
