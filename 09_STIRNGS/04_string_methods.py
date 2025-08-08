s = "Rayan"  # String are immutable 

# name[0] = "H" # You cannot change a character in a string directly

a = len(s)
print(a) # Length of the string

# common string methods

print(s.upper())  # Convert to uppercase
print(s.lower())  # Convert to lowercase
print(s.capitalize())  # Capitalize the first letter
print(s.title())  # Capitalize the first letter of each word

# Removing whitespace
text = "   Hello, World!   "
print(text.strip())  # Remove leading and trailing whitespace , output: "Hello, World!"
print(text.lstrip())  # Remove leading whitespace  ,output: "Hello, World!   "
print(text.rstrip())  # Remove trailing whitespace ,output: "   Hello, World!"

# find & replace
text = "Python is fun."
print(text.find("fun"))  # Find the index of a substring, output: 10
print(text.replace("fun", "awesome"))  # Replace a substring, output: "Python is awesome."

# Splitting and joining strings
text = "apple,banana,cherry"
fruits = (text.split(","))  # Split a string into a list
print(fruits) #output: ['apple', 'banana', 'cherry']
