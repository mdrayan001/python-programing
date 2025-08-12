s = {34,3,6,7,8,9,10}

# sets methods

s.add(100)  # Add an element
s.remove(3) # Remove an element, raises KeyError if not found
s.discard(6) # Remove an element, does not raise an error if not found
s.pop()  # remove random element 

print(s) # Output: {34, 6, 7, 8, 9, 10, 100}