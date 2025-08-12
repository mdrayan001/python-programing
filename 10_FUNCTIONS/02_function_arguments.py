# 1. postional arguments
def add1(a, b):  # here add(a,b) in function definition means that 'a' and 'b' are parameters
    x = a + b
    return x

c = add1(3, 4)  # we call the function with specific values or we can say we pass arguments to the function
print(c)

# 2. default arguments
def add2(a,b,plus = 0):  
    x = a + b + plus     # 'plus' is a default argument with a default value of 0
    return x

c = add2(3, 4, 5)  # we can pass a value for 'plus' or let it default to 0
print(c)

# 3. keyword arguments
def student(name, age, grade):
    print(f"Name: {name}, Age: {age}, Grade: {grade}")
    
student(age=20, name="Alice", grade="A")  # here we use keyword arguments to specify the order