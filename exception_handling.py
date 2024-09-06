## exceptions is a runtime error
a = 10
b = 0

c = None

try:
    c = a // b
    print(c)
except Exception as e:
    print("Error", e)

print("try except finished")

## multiple exception handling
l = [1, 5, 9, 7, 8, 6, 3, 5]

try:
    index = int(input("Input index"))
    print(l[index])
    print("no error")
except (ValueError, IndexError, Exception) as e:
    print("Error", e)
