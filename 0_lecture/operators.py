# Arithmetic Operators
print("sum :", 3 + 4)
print("difference :", 3 - 4)
print("product :", 3 * 4)
print("division :", 3 / 4)
print("floor division :", 3 // 4)
print("remainder :", 3 % 4)
print("exponentiation :", 3 ** 4)

# Assingment operators
n1 = 5
n2 = n1
print(n1 , n2)
n2 += n1
print(n1 , n2)
n2 -= n1
print(n1 , n2)
n2 *= n1
print(n1 , n2)
n2 /= n1
print(n1 , n2)

# Camparision Operators

n1 = 3
n2 = 7
print(n1 > n2) 

# Logical Operators
exp1 = 2 > 1 #True
exp2 = 5 < 4 # False
print("exp1 and exp2 :", exp1 and exp2) 
print("exp1 or exp2 :", exp1 or exp2) 
print("not exp1 :", not(exp1)) 

# membership operaters
fruits = ["apple", "banana", "cherry"]
print("if banana is present in fruits:", "banana" in fruits)
print("if mango is not present in fruits:", "mango" not in fruits)

#Bitwise Opreaters 
a = 3
b = 5 
print("a and b:", a & b )
print("a or b:", a | b )
print("a xor b:", a ^ b)
