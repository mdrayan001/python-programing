# Class: Class is a blueprint for creating objects. Eg. form for an exam that contains name , age , elective, father's name, mother's name, etc.

# Object: Object is an instance of a class. Eg. A student who has filled the form.

class Employee:
    company = "Google"  # Class variable, shared by all instances
    
    def get_salary(self): # Method to get salary and can be called on an instance , self refers to the instance
        return 10000
    
    
e = Employee()  # An object of Employee class
print(e.company)  # Accessing class variable
print(e.get_salary())  # Calling method to get salary

    
    