replace_str = "replacement word in string"

print(replace_str.replace("replace", "action"))

replace_str_multiple = "that is the same person and it is a good one also"

print(replace_str_multiple.replace("is", "test", 2))

join_iterable = ["hello", "world"]

print("--**--".join(join_iterable))

split = "bhanu is a good girl"

print(split.split())

control_split = "here are so many technologies for backend server development"

print(control_split.split(" ", 4))
print(control_split.split(" ", 2))

str_splitlines = '''checking splitlines method in 
                    python and 
                    why it will be used'''

print(str_splitlines.splitlines())