# dictionary comprehension allows for creating dictionaries in a concise way.

# example of dictionary comprehension

table_of_5 = {x: x * 5 for x in range(1, 11)}
print(table_of_5)  # Output: {1: 5, 2: 10, 3: 15, 4: 20, 5: 25, 6: 30, 7: 35, 8: 40, 9: 45, 10: 50}