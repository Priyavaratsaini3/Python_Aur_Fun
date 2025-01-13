import numpy as np

# 1. Create a NumPy array
array = np.array([1, 2, 3, 4, 5])
print("Array:", array)

# 2. Perform basic operations
print("Array + 2:", array + 2)
print("Array * 3:", array * 3)
print("Square of Array:", array ** 2)

# 3. Create arrays with specific patterns
zeros_array = np.zeros((2, 3))
print("\nZeros Array:\n", zeros_array)

ones_array = np.ones((3, 2))
print("\nOnes Array:\n", ones_array)

random_array = np.random.rand(3, 3)
print("\nRandom Array:\n", random_array)

# 4. Matrix operations
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

print("\nMatrix A:\n", matrix_a)
print("Matrix B:\n", matrix_b)

# Element-wise multiplication
print("Element-wise Multiplication:\n", matrix_a * matrix_b)

# Matrix multiplication
print("Matrix Multiplication:\n", np.dot(matrix_a, matrix_b))

# 5. Useful NumPy functions
print("\nMean of Array:", np.mean(array))
print("Standard Deviation of Array:", np.std(array))
print("Sum of Array:", np.sum(array))
print("Maximum Value in Array:", np.max(array))
print("Minimum Value in Array:", np.min(array))
