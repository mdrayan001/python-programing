age = int(input("Enter your age: " ))

if (age > 18):
    print("You can drive a car")
elif (age == 18):
    print("lets schedule a driving test")
elif (age ==0):
    print("You are just born")    
else:
    print("You cannot drive a car")
print("End of the program")  # This line is outside the if-elif-else block and will always execute