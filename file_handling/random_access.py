with open("my.data", "wb") as f:
    f.write("abcdefghi".encode())

with open("my.data", "rb") as f:
    print(f.read(2).decode())
    f.seek(3, 0)
    print(f.read(1).decode())
