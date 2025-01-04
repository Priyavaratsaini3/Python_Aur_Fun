num = int(input("Enter the positive number"))
if num % 15 == 0:
    print("number is divisible by 15")
else:
    if num % 3 == 0 or num % 5 ==0:
        print("number is not divisible 15 but divisible by 3 or 5")
    else:
        print("number is neither divisible by 3 nor by 5")