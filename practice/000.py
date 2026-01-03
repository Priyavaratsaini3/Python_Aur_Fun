# ## Dispaly the Output with the help of using print() function
# print("Hello World!")

# ## By defaulting print function using the end parameter 
# print("Hello")
# print("World")

# ## using the 'end' parameter
# print("Hello", end=" ")
# print("World ")

# ## using the 'end' with the '-' 
# print("Python", end="-")
# print("Programming")

# ## Using the 'sep' parameter 

# print("mango", "banana", "orange")
# print()
# print("mango", "banana", "orange", sep=',')

# ## Using the input function 

# # user_input = input("Hey, How are you ")
# # print("What's about you ", user_input)

# input = 23
# print(input)

# ## Store the string in a variable 
# str_variable = "prince saini"
# print(str_variable)

# ## Indentation : Structure of block 
# x = 11
# if x > 8:
#     print("x is greater than 11")
# else:
#     print("x is less than the 11")

# ## Multiple vairables Stored same value
# x = y = z = 444
# print(x, y, z)

# ## Using the one line of code for store the value in multiple variable in different and same value
# a, b, c = 11, 2, 3
# print(a, b, c)

# ## Data Type : Numbers
# ## Integer type 
# a = 23
# print(type(a))

# ## Float type number
# b = 12.3 
# print(type(b))

# ## Complex type Number
# c = 33+3j
# print(type(c))

# print(c.real)
# print(c.imag)

# ## type of a character and string 
# character = 'q'
# print(type(character))

# string = 'prince'
# print(type(string))


# str = 'python'
# new = sorted(str)
# print(new)
# new_str = ""
# neee = new_str.join(new)
# print(neee)

# ## swapcase

# str = 'python developer'
# str2 = str.replace('developer','learner')
# print(str2)

# txt = '-banana-'
# x = txt.strip('-')
# print(x)

list_1 = [1,2,3,4,5,6]
list_2 = ["hello", 35, 'abc', 4]

print(list_1 + list_2)

list3 = list_1*2
print(list3)