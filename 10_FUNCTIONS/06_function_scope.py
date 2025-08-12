def sum(a,b):
    # a and b are local variables
    c = a + b
    z = 1  # z is also a local variable which is destroyed after function execution
    return c

z = 8 # z is a global variable
print(z)
print(sum(10, 20 ))
print(z) # This will still print the global variable z

