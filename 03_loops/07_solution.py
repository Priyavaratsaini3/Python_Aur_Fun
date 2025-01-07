while True:
    number = int(input("Enter the value between 1 to 10 "))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else: 
        print("Invalid number, try again")