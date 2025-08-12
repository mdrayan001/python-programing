# Create a list contatining the table of 5 using list comprehension

a = 5 
table = [] # empty list to store the table

for i in range(1, 11):
    table.append(a * i)  # Append the product of a and i to the list
    
print(table)

# shortcut using list comprehension
table_comp = [a * i for i in range(1, 11)]  # List comprehension to create the table

print(table_comp)