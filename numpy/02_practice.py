# Array slicing 
import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])

arr = np.array([1,2,3,4,5,6,7])
print(arr[4:])

arr = np.array([1,2,3,4,5,6,7])
print(arr[:4])

arr = np.array([1,2,3,4,5,6,7])
print(arr[-3:-1])

arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5:2])

arr = np.array([1,2,3,4,5,6,7])
print(arr[::2])

# 2D array Slicing

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

arr = np.array([2,3,4,55])
print(arr.dtype)

arr = np.array([1,2,3,4,5,6,7], dtype='S')
print(arr)
print(arr.dtype)

arr = np.array([1,2,3,4,5,6,7], dtype='i4')
print(arr)
print(arr.dtype)

# arr = np.array(['a', '2', '3'], dtype='i')
# print(arr)

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

arr = np.array([1,0,3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

arr = np.array([1.11,2.34,3.55,4.5,5.5])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)