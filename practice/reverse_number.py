def reverse_number(num):
    result = 0
    sign = -1
    if num < 0:
        sign = 1
    else :
        sign = 1
    num = abs(num)
    for i in range(len(str(num))):
        result = result * 10 + num % 10
        num = num // 10
    return result * sign
print(reverse_number(120))