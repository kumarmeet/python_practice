import copy
from collections import Counter

dict1 = {"username": "john", "age": 28, "user_type": "admin", 44: "sector"}

print(dict1)

username = dict1.values()

print(dict1["username"])
print(dict1["age"])
print(dict1["user_type"])
print(dict1[44])

dict1["username"] = "wick"

dict1["jobs_applied"] = ("swe", "fullstack", "backend engineer")

print(dict1.values())
print(dict1.keys())

print(type(dict1["jobs_applied"]))

for i in dict1:
    print(f"{i} : {dict1[i]}")

del dict1["age"]

print(dict1)

## dictionary comprehension
dict2 = dict()

p = 1

for i in ["one", "two", "three"]:
    dict2[p] = i
    p += 1

print(dict2)

dict3 = dict(((1, "one"), (2, "two")))

print(dict3)

dict4 = dict(([1, "11"], [2, "22"], [3, "33"], [4, "44"]))
print(dict4)

dict5 = dict(("ab", "cd", "ef"))
print(dict5)

l1 = [1, 2, 3, 4]
l2 = [11, 22, 33, 44]
l3 = {"one", "two", "three"}

dict6 = dict(zip(l1, l2))
print(dict6)

dict7 = dict(zip(l1, l3))
print(dict7)

l5 = ['A', "B", "C"]

for item in enumerate(l5):
    print(item)

dict7 = dict(enumerate(l5))

print(dict7)

dict8 = {i: i ** 2 for i in range(1, 10)}

print(dict8)

dict9 = dict(((i, i ** 2) for i in range(1, 5)))

print(dict9)

dict10 = dict((x, y) for x, y in zip(l1, l3))

print(dict10)

dict11 = dict((item for item in enumerate(l5)))

print(dict11)

## looping over dictionary
for key, value in dict8.items():
    print(key, value)

for key in dict8.keys():
    print(key, dict8[key])

for value in dict8.values():
    print(value)

## dictionary methods
a = {1: 1, 2: 2, 3: [1, 2, 3, 4, 5]}

shallow_copy = copy.copy(a)
shallow_copy[3].append(44)
print(shallow_copy, a)

deep_copy = copy.deepcopy(a)
deep_copy[3].append(55)
print(deep_copy, a)

l4 = [5, 9, 8, 6]
dict_from_keys = dict.fromkeys(l4, True)
print(dict_from_keys)

## if key presents then get value otherwise create new key with none if not specified second arg
data = a.setdefault("testing", 456)
print(a, data)

a.pop("testing")
print(a)

a.popitem()
print(a)

a.clear()
print(a)

D = dict()

for x in enumerate(range(2)):
    D[x[0]] = x[1]
    D[x[1] + 7] = x[0]

print(D)

t = {1: 1, 2: 2}
p = {3: 3, 4: 4}

res = {**t, **p}

print(res)

t = "uiuioausdfoiuaisduiudf"

print(dict(Counter(t)))
