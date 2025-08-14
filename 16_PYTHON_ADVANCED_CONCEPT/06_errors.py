# while True:
#     try:
#         num1 = int(input("Enter first number: "))
#         num2 = int(input("Enter second number : "))
#         # print(f"The sum is {num1+num2}")
#         print(f"The division is {num1/num2}")
        
#     except ValueError:
#         print("Please dont perform bad typecasts")  
            
#     except ZeroDivisionError:
#         print("hey dont divide by 0")     
        
#     except Exception as e:
#         print("Unknown error occured!", e)        

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number : "))

if num2 == 0:
    raise ValueError("Please dont divide by 0")
print(f"The division is {num1/num2}")