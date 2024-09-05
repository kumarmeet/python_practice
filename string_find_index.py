str1 = "this is the same method"

print(str1.count("s"))
print(str1.count("is"))

print(str1.find("this"))
print(str1.find("is", 4, len(str1)))
print(str1.find("ok"))

print(str1.rfind("me"))
print(str1.rfind("sa", 0, 14))
print(str1.rfind("you"))

print(str1.index("this"))
print(str1.index("is", 4, len(str1)))
print(str1.index("ok"))

print(str1.rindex("me"))
print(str1.rindex("sa", 0, 14))
print(str1.rindex("you"))

