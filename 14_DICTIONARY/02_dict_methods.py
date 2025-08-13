# common dictionary methods

marks = {
    "Rayan": 89,
    "Harry": 76,
    "Emma": 91,
}

# print all the keys
print(marks.keys())  # Output: dict_keys(['Rayan', 'Harry', 'Emma'])

# print all the values
print(marks.values())  # Output: dict_values([89, 76, 91])

# print all the key-value pairs
print(marks.items())  # Output: dict_items([('Rayan', 89), ('Harry', 76), ('Emma', 91)])

# pop a key-value pair
marks.pop("Emma")
print(marks)  # Output: {'Rayan': 89, 'Harry': 76}