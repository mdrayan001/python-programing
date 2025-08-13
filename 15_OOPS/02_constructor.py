# constructor is a special method that is called when an object is created
# it is used to initialize the attributes of the object

class Employee:
    
    def __init__(self, salary, name,bond ):   # here __init__ is the constructor method
        self.salary = salary  # Instance variable, unique to each instance
        self.name = name      # Instance variable, unique to each instance
        self.bond = bond      # Instance variable, unique to each instance
        
    def get_info(self):
        print(f"The name of the employee is {self.name}, salary is {self.salary}, and bond is {self.bond} years.")
        
e1 = Employee(50000, "Alice", 2)  # Creating an object of Employee class with specific attributes
e1.get_info()  # Calling method to get employee information


        
    
    