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

print('5th element on 2nd row:',arr[1,4])

#3d array indexing
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print('3rd element of 2nd array of the 1st array :',arr[0,1,2])

# negative indexing
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1,-1])