## map helps to map the values

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]

res = map(lambda x, y: x + y, l1, l2)

for i in res:
    print(i, end=" ")

print("\n")

## max and min
print(max(l1))
print(min(l2))
print(min(5, 9, 8, 7, 3, 5, 4))
print(max("a", "f", "T", "R", "w"))

## join two iterators
ans = zip(l1, l2)

for x, y in ans:
    print(x, y)

## sum of list
print(sum(l1))

## sorted and give new reference

t = sorted(l1, reverse=True)
print(t)

## sort in same memory
l1.sort()
print(l1)

## check type of object
print(type(12))
print(type(12.5))
print(type("asc"))
print(type((1, 2)))
print(type({5, 7}))
print(type({5: 0, 7: True}))
print(type([1, 4, 5]))

## round the float numbers
print(round(123.56))
print(round(123.12345))

## pow give power of given number -> 2**4
print(pow(2, 4))
