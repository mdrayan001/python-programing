def divide(a,b):
    try:
        c = num1/num2
        print(c)
        return c
        
    except Exception as e:
        print(e)    
        return None

    # This is always executed no matter if try completely executes or not    
    finally:
        print("This is always executed")    
        
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number : "))        
divide(num1,num2)