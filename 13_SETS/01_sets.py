# Sets are unordered collections of unique elements. (no duplicates)
# They are mutable, meaning you can add or remove elements.
# Sets are defined using curly braces {} or the set() constructor.

# empty set
empty_set = set()

s = {1, 2, 3, 4, 5}
print(s,type(s))  
print(s[3])     # This will raise an error because sets do not support indexing