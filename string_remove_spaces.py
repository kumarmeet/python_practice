str1 = "python"

print(str1.ljust(10))
print(str1.ljust(10, "*"))
print(str1.rjust(10))
print(str1.rjust(10,"/"))
print(str1.center(10,))
print(str1.center(10,"$"))

str2 = "    python"

print(str2.lstrip())

str3 = "---- ... +++ aaa-python"

print(str3.lstrip("- .+a"))

str4 = "python          "

print(str4.rstrip())

str5 = "python---- ... +++ aaa-"

print(str5.rstrip("- .+a"))

str6 = "   python   "

print(str6.strip())

str7 = "---------python--------++////***"

print(str7.strip("-+/*"))

