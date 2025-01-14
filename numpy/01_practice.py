import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
print(np.__version__)

arr1 = np.array((1,2,3,4,5))
print(arr1)

# 0-D array
arr2 = np.array(42)
print(arr2)

# 1-D array
arr3 = np.array([1,2,3,4,5])
print(arr3)

# 2-D array
arr4 = np.array([[1,2,3], [4,5,6]])
print(arr4)

# 3-D array
arr5 = np.array([[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]])
print(arr5)

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)   
print(c.ndim)
print(d.ndim)

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimension: ', arr.ndim)

# array indexing

arr = np.array([1, 2, 3, 4])
print(arr[3])

print(arr[2] + arr[3])

#2d array indexing
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row:', arr[0, 1])