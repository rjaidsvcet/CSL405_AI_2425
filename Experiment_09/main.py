import numpy as np

# 1. Array Creation Techniques
print("1. Array Creation Techniques")

# a. Creating an array from a list
array_from_list = np.array([1, 2, 3, 4, 5])
array_from_list

# b. Using arange()
array_arange = np.arange(0, 10, 2)
array_arange

# c. Using linspace()
array_linspace = np.linspace(0, 10, 5)  # Divides 0 to 10 into 5 points
array_linspace

# d. Using zeros()
array_zeros = np.zeros((3, 3))
array_zeros

# e. Using ones()
array_ones = np.ones((2, 2))
array_ones

# f. Using eye() for identity matrix
array_eye = np.eye(3)
array_eye

# g. Using random() for random values
array_random = np.random.random((3, 3))
array_random

# 2. Different NumPy Methods
print("\n2. NumPy Methods")

# a. Reshaping an array
reshaped_array = np.arange(1, 10).reshape(3, 3)
reshaped_array

# b. Transposing an array
transposed_array = reshaped_array.T
transposed_array

# c. Mathematical operations
array_math = np.array([1, 2, 3])
array_math + 2
array_math * 3
np.sqrt(array_math)

# d. Aggregation methods
np.sum(array_math)
np.mean(array_math)
np.max(array_math)
np.min(array_math)

# e. Concatenation of arrays
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
concat_array = np.concatenate((array_a, array_b))
concat_array

# f. Sorting an array
unsorted_array = np.array([3, 1, 4, 2])
sorted_array = np.sort(unsorted_array)
sorted_array

# g. Indexing and Slicing
indexed_value = array_math[1]  # Indexing
indexed_value
sliced_array = array_math[1:3]  # Slicing
sliced_array

# h. Boolean Masking
boolean_mask = array_math > 2
boolean_mask
array_math[boolean_mask]
