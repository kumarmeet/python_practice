list1 = [1, 2, 3, 4, 5]
list2 = list(["a", "b", "c"])

print(list1, list2)

print(list1[4], list2[1], list1[-1], list2[-2])

list1[0] = "mutable"

list1.append(45)
list1.insert(1, 44)

print(list1)

## operators on list [], [:], *, +, in, not in

my_list = [1, True, {"user_name": "meet kumar"}, "flask"]

print(my_list[1:3])
print(my_list * 2)
print(my_list + [5, 6, 9, 7])
print("flask" in my_list)
print("football" not in my_list)

my_list.clear()

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(my_list[-1:-11:-1])
print(my_list[::-1])
print(my_list[0:11:2])
print(my_list[4:11])

my_list[0:4] = [40, 50, 60, 70]
print(my_list, len(my_list))

my_list[0:3] = [94, 85]
print(my_list, len(my_list))

my_list[0:1] = [66, 54, 23, 98, 75, 100, 123]
print(my_list, len(my_list))

## length of list / step when perform steps updating the list
my_list[::3] = ["hello", "hello", "hello", "hello", "hello"]
print(my_list, len(my_list))

product_price = [12.15, 48.65, 74.98, 12.65, 44.23]
product_selling_price = [14, 50, 90, 15, 50]

concat_data = product_price + product_selling_price

print(concat_data, sum(concat_data))

## list comprehensions

l1 = [x for x in range(10)]

print(l1)

l2 = [x * 2 for x in range(1, 11)]

print(l2)

l3 = [x for x in concat_data if x < 50]

print(l3)

l4 = [x for x in "iadkfja&*as;jdkjfieop" if x.isalpha()]

print(l4)
