import numpy as np

x = [1,2,3,4]

y = np.array(x)

print(y)
print(type(y))
print(y.ndim)

# l = []

# for i in range(1,5):
#     int_1 = int(input("Enter: "))
#     l.append(int_1)

# print(np.array(l))

arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)
print(arr2.ndim)

arr3 = np.array([[[1,2,3,4], [2,3,4,5], [3,45,6,6]]])
print(arr3) 
print(arr3.ndim)

arn = np.array([1,2,3,4], ndmin=10)
print(arn)
print(arn.ndim)