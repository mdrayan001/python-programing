# a = 4
# b = 5
# c = 2

# average = (a+b+c)/3
# print(average)

# Function syntax

def average(a, b, c):   # here we define a function named 'average' that takes three parameters
    """Calculate the average of three numbers."""
    d= (a + b + c) / 3  
    # print(d) # 
    return d

# Calling the function
result = average(4, 5, 2)  # we call the function with specific values
print(result)  # this will print the result of the function call
