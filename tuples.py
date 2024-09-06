tup1 = (*(x for x in range(1, 10)),)

tup2 = tuple((1, 2, 3, 4, 5, 6, 7, 8, 9))

print(tup1, tup2)

tup3 = tuple([1, 2, 3, 4, 5, 6])

print(tup3 * 2)

tup4 = 4, 5, 6, 9, 8, 7, 3

print(tup4)

a, b, c, *d = tup4

print(a, b, c, d, type(d))

print(tup4[0:2] + (5, 6, 7, 8), tup3[1])