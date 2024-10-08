## abs gives always positive value

a, b = -15, -14.5
print(abs(a), abs(b))

## convert anything into ascii
print(ascii("\u0521"))

## convert an integer into binary form
print(bin(14))

## convert into boolean
print(bool(10))
print(bool(0))

##convert string into bytearray (mutable)
ba = bytearray(5)
print(ba)
s1 = "abcde"
ba = bytearray(s1.encode())
print(ba)
for i in ba:
    print(i)

##convert string into bytearray (immutable)
ba = bytes(5)
print(ba)
s1 = "abcde"
ba = bytes(s1.encode())
print(ba)
for i in ba:
    print(i)


## return boolean if callable arg will be a func
def func():
    print("callable")


print(callable(func))
print(callable(ba))

## convert ascii code to char of given ascii number
print(chr(97))
print(chr(122))

## convert char to ascii of given char
print(ord("A"))
print(ord("e"))

# print(help("modules"))

## divmod gives remainder and quotient

quotient, remainder = divmod(11, 3)
print(quotient, remainder)

## enumerate gives a indexing of a given iterable

l = [5, 9, 8, 6, 3, 7]
t = (4, 3, 7)
s = {3, 4, 7, 6}
d = {1: 6, "name": "meet"}
enl = enumerate(l)
ent = enumerate(t)
ens = enumerate(s)
endi = enumerate(d)

for i, j in enl:
    print(i, j)

for i, j in ent:
    print(i, j)

for i, j in ens:
    print(i, j)

for key, value in endi:
    print(key, value)

## executing string expression
print(eval("2**4"))

## it executes the python statements
exec("x=10\nb=20\nprint('x and b sum is', x+b)")
