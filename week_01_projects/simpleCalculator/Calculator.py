def addition(x,y):
    return x+y 

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def division(x,y):
    if (y == 0):
        return "Error ! Division by zero."
    return x/y

#main

print("Welcome to the Simple Calculator!")
while(True):
    try:
        num1 = float(input("Enter the First number: "))
        operation = input("Enter the opertaion (+,-,*,/): ").strip()
        num2 = float(input("Enter the second number: "))

        if(operation =='+'):
            result = addition(num1,num2)
        elif(operation == '-'):
            result = subtract(num1,num2)
        elif(operation == '*'):
            result = multiply(num1,num2)
        elif(operation == '/'):
            result = division(num1,num2)
        else: 
            result = "Invalid Operation Selected"
        print(f"The Result is : {result}")

    except ValueError:
        print("Invalid Number ! Please Enter Numaric Number:")

# Ask user to if you want to continue 
    cont = input("Do you want to perfom another Calculation (yes/no)!:").lower().strip()

    if cont == 'yes':
        continue
    elif cont == 'no':
        print("Thank you for using Caculator! Good Bye!")
        break

    else:
        print("Invalid Input!")
        break
