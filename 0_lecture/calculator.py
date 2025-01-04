num1 = int(input("Enter the number1 :"))
num2 = int(input("Enter the number2 :"))

operator = input("Enter the operator")

match operator:
    case "+":
        print("Sum is", num1 + num2)
    case "-":
        print("Difference is", num1 - num2)
    case "*":
        print("Product is", num1 * num2)
    case "/":
        print("Division is", num1 / num2)
    case _:
        print("Enter a valid operator") 