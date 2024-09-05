a = {1, 2, 3, 4, 5, 7}

b = {5, 7, 9, 10, 11}

## union
c = a.union(b)
print(c)
c = a | b
print(c)

## intersection
d = a.intersection(b)
print(d)
d = a & b
print(d)

## difference
e = a.difference(b)
print(e)
e = a - b
print(e)
e = b.difference(a)
print(e)
e = b - a
print(e)

## symmetric difference
f = a.symmetric_difference(b)
print(f)
f = a ^ b
print(f)

g = {1, 2, 3, 4}

h = a.issubset(g)
print(h)
h = g.issubset(a)
print(h)
i = a.issuperset(g)
print(i)

g.add(10)
g.add((22, 33, 55)) ## only can add tuples

print(g)

j = g.copy()

print(j)

j.discard(3)
print(j)

j.pop()
print(j)

g.clear()
print(g)

## comprehension
res = {x for x in "hello world"}
print(res)
res = {x for x in {4, 5, 9, 7, 8, 6, 3, 5, 4, 2, 1, 8, 9, 7, 7, 7}}
print(res)
