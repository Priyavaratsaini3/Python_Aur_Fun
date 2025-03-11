# python program to convert into decimal number system 
n1 = "17"
n2 = "1110010"
n3 = "1c2"

n = int(n1 , 8)
print("Octal 17 = ", n)

n = int(n2 , 2) 
print("Binary 1110010 = ", n)

n = int(n3 , 16)        
print("Hexadecimal 1c2 = ", n)

a = 10
b = bin(a)
print(b)

b = oct(a)
print(b)

b = hex(a)
print(b)