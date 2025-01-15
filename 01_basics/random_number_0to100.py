import random 
random_number = random.randint(0,100)
print(random_number)
if random_number % 2 == 0:
    print("The number is even:", random_number)
else: 
    print("The number is odd:", random_number)