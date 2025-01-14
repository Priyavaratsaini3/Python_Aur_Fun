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