# continue statement in loops
# using continue to skip the current iteration and continue with the next one

for i in range(1, 11):
    if i == 5:
        continue  # Skip the rest of the loop when i equals 5
    print(i)
    
# This will print numbers from 1 to 4 and then skip 5, continuing with 6 to 10.    
    