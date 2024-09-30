'''
1. Lists
* Create a list of numbers, then double each value.
* Remove duplicates from a list.
* Sort a list of tuples by the second value.
* Find the index of an item in a list.
* Reverse a list without using the reverse() function.
* Merge two lists into one.
* Filter out all even numbers from a list.
* Find the largest and smallest number in a list.
* Flatten a list of lists into a single list.
* Count the frequency of each element in a list.
'''


def double_of_list(l1):
    return [x * 2 for x in l1]


def remove_duplicates(l1):
    return list(set(l1))


def sort_tuples_by_second(l1):
    return sorted(l1, key=lambda x: x[1])


def index_of_item(l1, item):
    return l1.index(item)


def reverse_list(l1):
    return l1[::-1]


def merge_lists(l1, l2):
    return l1 + l2


def event_lists(l1):
    return list(filter(lambda x: x % 2 == 0, l1))


def largest_smallest_number(l1):
    return min(l1), max(l1)


def flatten_list(l1):
    return sum(l1, [])


def count_frequency(l1):
    res = {}
    for i in l1:
        res[i] = res.get(i, 0) + 1
    return res


if __name__ == "__main__":
    print(double_of_list([1, 2, 3, 4, 5]))
    print(remove_duplicates([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
    print(sort_tuples_by_second([(1, 2), (3, 2), (4, 1)]))
    print(index_of_item([1, 2, 3, 4, 5], 3))
    print(reverse_list([1, 2, 3, 4, 5]))
    print(merge_lists([1, 2, 3, 4, 5], [6, 7, 8, 9]))
    print(event_lists([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(largest_smallest_number([1, 2, 3, 4, 5]))
    print(flatten_list([[1, 2, 3], [4, 5, 6]]))
    print(count_frequency([1, 3, 6, 5, 1, 4, 3, 3, 5]))
