## string operators

first_name = "meet"
middle_name = "kumar"
last_name = "vishwakarma"

words = f"{first_name} {middle_name} {last_name}".split(" ")

full_name = ""

for i in words:
    full_name += " " + i.capitalize()

print(full_name.strip())

won = "won " * 3

print(won)

if "Meet" in full_name:
    print("Yes this is correct")

if "hello" not in full_name:
    print("Yes this is not in correct")

s1 = "hello" "world"

print(s1)

s2 = "new" + str(18)

print(s2)

s4 = "hello world"

## slicing [start : end : step]
print(s4[::])
print(s4[-1::-1])
print(s4[::-1])
print(s4[0:len(s4):])
print(s4[0:6:])
print(s4[0:len(s4):2])
print(s4[-1::-4])


#string methods
# print(dir(str))

str_func = "          classes have functions And properties"
# help(str_func.isspace)

print(str_func.replace("s","S"))
print(str_func.count("s"))
print(str_func.split(" "))
print(" ".join(str_func.split(" ")))
print(str_func.strip())
print(str_func.upper())
print(str_func.lower())
print(str_func.find("have"))
print(str_func.isspace())