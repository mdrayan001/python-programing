def sum(a,b):
    print("Hey I am summing")
    c = a + b
    global z  # please modify globlal variable z
    z =0  # This will print the modified global variable z
    return c

z = 3  # z is a global variable
print(sum(3,12))
print(z)
