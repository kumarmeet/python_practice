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

## try except else

try:
    index = int(input("Input index"))
    print(l[index])
    print("no error")
except (ValueError, IndexError, Exception) as e:
    print("Error", e)
else:
    print("Try block executed successfully")

## finally block (mainly useful inside the function)

try:
    index = int(input("Input index"))
    print(l[index])
    print("no error")
except (ValueError, IndexError, Exception) as e:
    print("Error", e)
    raise Exception
else:
    print("Try block executed successfully")
finally:
    print("It guarantee this finally block always executed")


## user defined exceptions
class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    raise MyError("My user defined error")
except MyError as e:
    print("Error", e)

## nested try and catch
