import json

file = open("write-data.txt", "r")

print(file.name)

print(file.mode)

print(file.closed)

print("First line -> ", file.readline(), end="")
print("Second line ->", file.readline())

print(file.readable())

print(file.tell())

file.close()

lines = open("file_modes.py", "r")

update_file = open("my-data.txt", "a")

for line in lines:
    if line in lines:
        continue
    update_file.write("\n" + line)
    print(line, end="")
else:
    print("File closed")
    file.close()
    update_file.close()

json_file = open("data.json", "w+")

data = [{"name": "meet kumar", "id": 44}, {"name": "john", "id": 10}]
json.dump(data, json_file, indent=4)
