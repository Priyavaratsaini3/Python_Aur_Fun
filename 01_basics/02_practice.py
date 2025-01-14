import math

# Write a multi-line Python program to calculate the area of a circle using the formula:
# Area = π × r²
# Use r = 7 and print the result.
r = 7 
Area = int(math.pi) * r**2
print(Area)

# Fix the syntax errors in this code snippet:
print("Welcome to Python")
x = 10
y = 20
print(x + y)

# Add comments to explain the purpose of this program:
# This program adds two numbers
x = 5
y = 3
print(x + y)

# Write a Python program to display the following output. Use a comment to describe what each line does:
# Hello
# Welcome to Python!

print("Hello") # This line is the print the output hello 
print("Welcome to Python!") # This line is the print output Welcome to Python!

# Write a program that calculates the sum of three numbers, but make sure you comment out one of the numbers so it isn’t included in the sum.

x = 10
y = 20
# z = 30
sum = x + y
print(sum)

# Declare variables to store the following information about yourself and print them:
# Name
# Age
# Favorite color
# Country

Name = "Priyavart saini"
Age = 21
Favorite_color = "Red"
Country = "India"
print(Name, Age, Favorite_color, Country)

# Swap the values of two variables and print their values before and after swapping.
# Example:
# x = 10
# y = 20
# # Your code here
# print("After swapping:", x, y)

x = 10
y = 20 
print("Before swapping:", x, "\n", y)
x, y = y, x
print("After swapping:", x, "\n", y)

# Write a program that calculates and prints the perimeter and area of a rectangle. Take the length and width as variables.

length = 10
width = 20
perimeter = 2 * (length + width)
area = (length * width)
print(perimeter, area)

# For each data type, create an example:
# int: Assign an integer value to a variable and print it.
# float: Assign a float value and print it.
# str: Assign a string and print it.
# list: Create a list of your 3 favorite fruits and print it.
# tuple: Create a tuple of 3 numbers and print it.
# set: Create a set of 3 unique numbers and print it.
# dict: Create a dictionary with keys as subjects and values as grades. Print it

x = 10
print(x) # int
y = 10.5
print(y) # float
z = "Priyavart saini"
print(z) # str
fruits = ["Apple", "mango", "banana"]
print(fruits) # list
numbers = (1, 2, 3)
print(numbers) # tuple
numbers = {1, 2, 3}
print(numbers) # set
subjects = {"English": 90, "Maths": 80, "Science": 70}
print(subjects) # dict

# Write a Python program to check the data type of the following variables:
# python
# Copy code
# x = 42
# y = "Hello, Python!"
# z = [1, 2, 3, 4]

x = 42
print(type(x))
y = "Hello, Python!"    
print(type(y))
z = [1, 2, 3, 4]
print(type(z))

# Write a program that converts:
# A float to an integer.
# An integer to a string.
# A string to a list of characters.

x = 2.23 
y = int(x)
print(y)
z = 4
a = str(z)
print(a)
print(type(a))

b = "a", "b", "c"
list1 = list(b)
print(list1)