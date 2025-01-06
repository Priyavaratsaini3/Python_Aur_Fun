age = int(input("Enter the Age: "))
day = str(input("Enter the Day: "))

price = 12 if age >= 18 else 8

if day == "wednesday":
    price -= 2

print("Ticket price for you is $", price)