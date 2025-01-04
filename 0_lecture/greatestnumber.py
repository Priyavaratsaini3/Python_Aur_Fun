n1 = int(input("Enter the number 1:"))
n2 = int(input("Enter the number 2:"))
n3 = int(input("Enter the number 3:"))

## if n1 is greatest number
#if n1 > n2 and n1 > n3:
#    print(n1, "is the Greatest number")
#
## if n2 is the greatest number
#elif n2 > n1 and n2 > n3:
#    print(n2,"is the Greatest number")
#
## if n3 is the greatest number
#else:
#    print(n3,"is the Greatest number")
if n1 > n2:
    if n1 > n3:
        print(n1,"is the greatest number")
    else:
        print(n3,"is the greatest number")
else:
    if n2 > n3:
        print(n2,"is the greatest number")
    else:
        print(n3,"is the greatest number")