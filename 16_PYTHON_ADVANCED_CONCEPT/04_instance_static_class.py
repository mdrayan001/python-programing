class Employee:
    company = "HP"
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary
    # instance method    (default)
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)
    # Static method
    @staticmethod
    def sum(a,b):
        return a+b    
    # class method
    @classmethod
    def print_company(cls):
            print(cls.company)
    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company
         
                      
e1 = Employee("Rayan", 45689)
e2 = Employee("ferzin",34566)
print(Employee.company)  
#print(Employee.name)  # this will through error

e1.print_info()    
e2.print_info()

print(e2.sum(4,5))
e1.print_company()
e1.change_company("acer")
print(Employee.company)