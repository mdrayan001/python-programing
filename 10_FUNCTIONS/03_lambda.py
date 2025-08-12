# lambda functions are small anonymous functions defined with the lambda keyword.

square = lambda x: x * x  
'''
As good as writing:
def square(x):
    return x * x
'''
print(square(5))  # Output: 25

sum = lambda a, b: a + b
'''
As good as writing:
def sum(a, b): 
    return a + b
'''
print(sum(3, 4))  # Output: 7