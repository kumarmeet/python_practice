j = 0

while j <= 10:
    print(j)
    j += 1
    if j == 3:
        break
else:
    print("Loop is finished")

txt = "hello world"

for i in txt:
    print(i , " <-")

for i in range(0, len(txt), 2):
    print(txt[i])

for i in range(0, 4):
    print(i)

for j in range(len(txt) - 1, 0, -1):
    if txt[j] in txt:
        print(txt[j])

for num in range(1, 11):
    print(2 * num)

fact = 5
res = 1

for num in range(1, fact + 1):
    res *= num

print(res)