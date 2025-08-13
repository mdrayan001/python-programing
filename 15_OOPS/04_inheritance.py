# inheritance are inheriting the properties of another class

class Animal:
    location = "India"    # Class variable, shared by all instances
    def __init__(self, name):  # Constructor method to initialize the instance variable
        self.name = name 
        
    def speak(self):      # Method to be overridden in subclasses
        print(f"{self.name} makes a sound")
        
class Dog(Animal):  # Dog class inherits from Animal class
    def speak(self):  # Overriding the speak method
        super().speak()  # we are using the speak function of the parent class 
        print(f"{self.name} barks")
        
        
# a = Animal("Dog")
# a.speak()  # Calling the speak method of Animal class
d = Dog("Buddy")  # Creating an instance of Dog class
d.speak()  # Calling the overridden speak method of Dog class  
print(d.location)