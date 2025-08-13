class Employee:
    company = "Asus"  # Class variable, shared by all instances
    
    def __init__(self, salary, name,bond,company ):   # here __init__ is the constructor method
        self.salary = salary  # create an instance attribute of name salary and assign it with slary
        self.name = name      
        self.bond = bond 
        self.company = company     
        
    def get_info(self):
        print(f"The name of the employee is {self.name}, salary is {self.salary}, and bond is {self.bond} years.")
        
e1 = Employee(50000, "Alice", 2 ,"Tesla")  # Creating an object of Employee class with specific attributes
print(e1.company) # will alway print instance attribute whenever present 
print(Employee.company)  # this will always print class variable or attribute

# object introsepection
print(dir(e1))  # This will show all attributes and methods of the instance e1
