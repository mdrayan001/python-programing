a = {3,23,1}
b = {34,56,78,21,3}

# Set operations: union, intersection, difference, symmetric difference

c = a.union(b) # contains all unique elements from both sets along with duplicates removed
print("Union:", c)  # output: {1, 3, 21, 23, 34, 56, 78}

d = a.intersection(b) # contains only elements that are present in both sets
print("Intersection:", d)  # output: {3}

e = a.difference(b) # contains elements that are in set a but not in set b
print("Difference:", e)  # output: {1, 23}

f = a.symmetric_difference(b) # contains elements that are in either set but not in both
print("Symmetric Difference:", f)  # output: {1, 21, 23, 34, 56, 78}
