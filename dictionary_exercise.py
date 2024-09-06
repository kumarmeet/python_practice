## find birthday of a person

# birthday = {"meet": "2022-07-1990", "meet1": "2022-07-1991", "meet2": "2022-07-1995"}
#
# input_data = input("Input key -> ")
#
# if input_data in birthday:
#     print(birthday[input_data])
# else:
#     print("Wrong input")

## create a list of country names in alphabetical order

countries = {"a": ["America", "Alaska", "Argentina"], "b": ["Bhutan", "Brazil", "Bahrain"],
             "c": ["Costa Rica", "China", "Cuba"]}

for keys in countries:
    countries[keys] = sorted(countries[keys])

print(countries)
