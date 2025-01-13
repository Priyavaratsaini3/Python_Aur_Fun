import timeit
import numpy as np

# Define functions for the tasks
def list_comprehension():
    return [j**4 for j in range(1, 9)]

def numpy_operation():
    return np.arange(1, 9)**4

# Measure execution time
x = timeit.timeit(list_comprehension, number=10)
y = timeit.timeit(numpy_operation, number=10)

print(f"{x} vs {y}")
