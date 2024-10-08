from typing import Dict, List, Union


def find_planet_name_by_id(planet_id, planets_data: Dict):
    return planets_data[planet_id]


# Create a dictionary of planets with their corresponding IDs
planets = {
    1: "Mercury",
    2: "Venus",
    3: "Earth",
    4: "Mars",
    5: "Jupiter",
    6: "Saturn",
    7: "Uranus",
    8: "Neptune",
    9: "Pluto"  # Even though Pluto is classified as a dwarf planet, it's included here.
}

print(find_planet_name_by_id(9, planets))


## sum of scores ending with zero

def sum_ending_zero(l: List[int]):
    return sum([i for i in l if i % 10 == 0])


L = [10, 45, 200, 600, 70, 782]

print(sum_ending_zero(L))


## invert the dic key becomes value and values become keys

def invert_dict(d1: Dict):
    return {v: k for k, v in d1.items()}


print(invert_dict(planets))


## find the string is pangram or not

def is_pangram(s: str):
    alpha = set("abcdefghijklmnopqrstuvwxyz")
    s = s.lower()
    phrase = set(s)
    if alpha.issubset(phrase):
        return True
    else:
        return False


print(is_pangram("The quick brown fox jumps over the lazy dog"))


## count upper and lowercase letter

def count_upper_and_lower(s: str):
    upper = 0
    lower = 0

    for i in s:
        if i.isupper():
            upper += 1
        if i.islower():
            lower += 1

    return upper, lower


print(count_upper_and_lower("Hello World"))


##find minimum with variable arg
def find_minimum_max(*args, low_limit=0, flag: str):
    if low_limit is None:
        return min(args) if flag == "min" else max(args)
    return min([x for x in args if x >= low_limit]) if flag == "min" else max([x for x in args if x >= low_limit])


print(find_minimum_max(1, 5, 2, -5, 10, 12, 9, low_limit=2, flag="min"))
print(find_minimum_max(1, 5, 2, -5, 10, 12, 9, low_limit=9, flag="max"))

## flatten list

T = List[Union[int, List['T']]]


def flatten_list(nested_list: T) -> List[int]:
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))  # Recursively flatten
        else:
            flat_list.append(item)
    return flat_list


# Example nested list
L2: T = [1, 2, 3, [4, 5, 6], 7, 8, [9, 10], 11, [12, 13, [14, 15, 16]]]

print(flatten_list(L2))
