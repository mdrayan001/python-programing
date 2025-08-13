# Dictionary store key-value pairs and allow for fast lookups.
# They are mutable and unordered collections in Python.

# empty dictionary
empty_dict = {}

# Creating a dictionary with some initial key-value pairs
marks = {
    "John": 85,
    "Alice": 92,
    "Bob": 78,
    "Diana": 88
}

print(marks, type(marks))

# Accessing values using keys
print(marks["Alice"])  # Output: 92

# changeing a value
marks["Bob"] = 80
print(marks["Bob"])  # Output: 80

# Adding a new key-value pair
marks["Eve"] = 95
print(marks)  # Output: {'John': 85, 'Alice': 92, 'Bob': 80, 'Diana': 88, 'Eve': 95}
