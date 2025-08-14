def marks(**kwargs):
    # kwargs is a dictionary with all the key value pairs which were passed to marks
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")

# Example usage
marks(shubham=34,rayan = 98, harry = 97,rani =78)