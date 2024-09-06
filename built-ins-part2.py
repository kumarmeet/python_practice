## gives iterable object after filtering data
l = [3, 6, 7, 9, 12, 19, 21]


def odd(x):
    if x % 2 != 0:
        return True
    else:
        return False


res = filter(odd, l)

for i in res:
    print(i, end=" ", )

print("\n")

lam = filter(lambda X: X % 2 == 0, l)

print(next(lam))
print(next(lam))

## it converts the format given value
print(format(10, "b"))
print(format(0b101010, "d"))
print(format(97, "c"))

## convert any set into immutable set
se = frozenset({5, 9, 7, 6, 3})
print(se)

## give all global variables
print(globals().keys)

## find out if an object having a given attribute or not
str1 = "abcde"
print(hasattr(str, "lower"))
print(hasattr(str, "isalpha"))
print(hasattr(str, "total"))

## every object in python has its own hash value
print(hash(str1))
print(hash(lam))

## help method show the description of object

help(str1.format)
help(str1.encode)

## every object has its own id in python
print(id(str1))
print(id(lam))

## check an instance of a particular class or not
print(isinstance(str1, str))
print(isinstance(lam, filter))
print(isinstance(lam, int))

## iter give a iterable object
it = iter(l)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
