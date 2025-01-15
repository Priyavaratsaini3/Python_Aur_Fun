# Numpy version print 
import numpy as np
print("Numpy version: ",np.__version__)

# Create a 1D NumPy array containing numbers from 1 to 5.
# Print the array and its type.

arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Type: ", type(arr))

#Create a 2D NumPy array:
arr2 = np.array([[1, 2, 3,], [4, 5, 6]])
print(arr2)

# #Print the following attributes:
# Shape
# Data type
# Number of dimensions (ndim).

print("Shape:", arr2.shape)
print("Data Type:", arr2.dtype)
print("Number of Dimensions:", arr2.ndim)

# Create a 2D array:
# [[10, 20, 30],
#  [40, 50, 60]]
# Access the element in the second row, third column.

arr3 = np.array([[10, 20, 30], [40, 50, 60]])
print(arr3)
print("Element in second roe and third column: ",arr3[1, 2])

# Exercise 5: Slicing Arrays
# Create an array:
# [10, 20, 30, 40, 50, 60]
# Extract the sub-array [20, 30, 40]

arr4 = np.array([10, 20, 30, 40, 50, 60])
print("Extracted the sub-array: ",arr4[2:5])

# Exercise 6: Array from Python List
# Create a NumPy array from the Python list:
# [1, 2, 3, 4, 5]

list1 = [1, 2, 3, 4, 5]
arr5 = np.array(list1)
print("Array from Python list: ", arr5)

#Exercise 7: Array of Zeros
# Create a 3x3 array filled with zeros.

arr6 = np.zeros((3, 3))
print("Array of Zeros: \n", arr6)

# Exercise 8: Array of Ones
# Create a 2x4 array filled with ones.

arr7 = np.ones((2, 4))
print("Array of Ones: \n", arr7)

# Exercise 9: Array with a Range
# Create an array of integers from 10 to 50 (inclusive).
arr8 = []
for i in range(10,51):
    arr8.append(i)
print("Array with a Range: ", np.array(arr8))

# Exercise 10: Array wit h Evenly Spaced Numbers
# Create an array of 5 evenly spaced numbers between 0 and 1.

arr9 = np.linspace(0,1, num=5)
print(arr9)

# Exercise 11: Identity Matrix
# Create a 4x4 identity matrix.

arr10 = np.identity(4)
print("Identity matrix 4X4 :\n",arr10)

# Exercise 12: Random Numbers
# Create a 3x3 array with random values between 0 and 1.

arr11 = np.random.rand(3,3)
print(arr11)

# Exercise 13: Reshaping Arrays
# Create a 1D array of numbers from 1 to 12.
# Reshape it into a 3x4 array.

arr12 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr12)
print(arr.ndim)
x = arr12.reshape(3,4)

print(x)
print(x.ndim)
