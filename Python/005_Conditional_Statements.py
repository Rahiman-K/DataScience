# Conditional Statements

# IF STATEMENT

a = 12
if a == 12:
    print('Correct')
    

# ELIF STATEMENT

if a == 3:
    print("Not Correct")
elif a == 12:
    print("Twelve")

# ELSE STATEMENTS

b = "I Don't Care"

if a == 1:
    print("One")
elif a == 2:
    print("Two")
else:
    print(b)
    

# Nested Conditional Statements

num  = int(input("Enter the number : "))
if num > 0:
    print("The number is positive")
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
        
else:
    print("The number is negative or zero")
        
        
        
## Year eg:
    
year = int(input("Enter the Year  : "))

if year%4==0:
    if year%100 == 0:
        if year%400 == 0:
            print(year," is a leap year")
        else:
            print(year, " is not a leap year")
            
    else:
        print(year," is a leap year")
else:
    print(year," is not a leap year")
                
