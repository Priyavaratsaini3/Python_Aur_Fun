# # Ask to user for their name
# name = input("what is your name? ").strip().title()

# first, last = name.split(" ")

# # Say Hello to user
# print(f"hello, {first}")

# x = input("What's x? ")
# y = input("What's y? ")

# z = int(x) + int(y)

# print(z)

# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = round(x + y)
# z = round(x / y , 2)
# z = x / y

# print(f"{z:.2f}")
# print(z)
# print(f"{z:,}")

# def hello(to='World'):
#     print("Hello," , to)
# hello()
# name = input("What's your Name: ")

# hello(name)

# def main():
#     name = input("What's your Name: ")
#     hello(name)

# def hello(to='world'):
#     print("hello", to)

# main()

# def main():
#     x = int(input("What's x? : "))
#     print("x squared is :", square(x))

# def square(n):
#     return pow(n, 2)

# main()

# x = int(input("What's x ? : "))
# y = int(input("What's y ? : "))

# if x > y:
#     print("x is greater than y")
# elif x < y:
#     print("x is less than y")
# else:
#     print("x is equal y")

# if x > y or x < y:
#     print("x is not equal y")
# else:
#     print("x is equal y")

# if x == y:
#     print("x is equal y")
# else:
#     print("x is not equal y")

# score = int(input("Score : "))

# if 90 <= score:
#     print("Grade: A")
# elif 80 <= score:
#     print("Grade: B")
# elif 70 <= score:
#     print("Grade: C")
# elif 60 <= score:
#     print("Grade: D")
# else:
#     print("Grade: F")

# x = int(input("What's x? "))

# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# def main():
#     x = int(input("What's x ? :"))

#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")

# # def is_even(n):
# #     if n % 2 == 0:
# #         return True
# #     else:
# #         return False

# def is_even(n):
#     return n % 2 == 0

# main()

# name = input("What's your Name? :")

# if name == "Harry":
#     print("Gryffindor")
# elif name == "Hermione":
#     print("Gryffindor")
# elif name == "Ron":
#     print("Gryffindor")
# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

# match name:
#     case "Harry" | "Hermione" | "Ron":
#         print("Gryffindor")
#     # case "Hermione":
#     #     print("Gryffindor")
#     # case "Ron":
#     #     print("Gryffindor")
#     case "Draco":
#         print("slytherin")
#     case _:
#         print("Who?")

## Contional loops

# i = 3 
# while(i != 0):
#     print("meow")
#     i = i - 1

# i = 0
# while(i < 3):
#     print("meow")
#     i  += 1

# for i in  [0, 1, 2]:
#     print("meow")

# for _ in range(3):
#     print("meow")

# print("meow\n"*3 )

# while True:
#     n = int(input("what's n?"))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")

# def main():
#     number = get_number()
#     meow(number)
# def get_number():
#     while True:
#         n = int(input("what's n?"))
#         if n > 0:
#             break
#     return n
    

# def meow(n):
#     for _ in range(n):
#         print("meow")

# main()

# students = ["Hermione", "Harry", "Ron"]

# # print(students[0])
# # print(students[1])
# # print(students[2])

# # for student in students:
# #     print(student)

# for i in range(len(students)):
#     print(i + 1, students[i])

# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin"
# }

# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

# for student in students:
#     print(student, students[student], sep=", ")

# students = [
#     {"Name": "Hermione", "House": "Gryffindor", "Patronus": "Otter"},
#     {"Name": "Harry", "House": "Gryffindor", "Patronus": "Stag"},
#     {"Name": "Ron", "House": "Gryffindor", "Patronus": "Jack Russell terrier"},
#     {"Name": "Draco", "House": "Slythein", "Patronus": None}
# ]

# for student in students:
#     print(student["Name"], student["House"], student["Patronus"], sep=",")

# def main():
#     print_row(4)
# #     print_column(3)

# # def print_column(height):
# #     for _ in range(height):
# #         print("#")

# def print_row(width):
#     for _ in range(width):
#         print("?",end="")
    
# main()


# def main():
#     print_square(3)

# def print_square(size):
#     ## For each row in square
#     for i in range(size):
#         ## For each brick in row
#         for j in range(size):
#             ## print Brick
#             print("#", end="")
#         print()

# main()

# def main():
#     print_square(4)

# def print_square(size):
#     for i in range(size):
#         print_row(size)

# def print_row(width):
#     print("#" * width)

# main()

# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not a integer")
# else:
#     print(f"x is {x}")

# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             x = int(input("What's x?"))
#         except ValueError:
#             print("x is not a integer")
#         else:
#             break
#     return x

# main()

def main():
    x = get_int("What's x?")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()


