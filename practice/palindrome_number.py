import math
def isPalindrome(x):
    if x < 0:
        return False
    elif x == 0:
        return True
    else:
        rev = 0
        temp = x
        while temp > 0:
            rem = temp % 10
            rev = rem + rev * 10
            temp = temp // 10
        return rev == x 

print(isPalindrome(787))

