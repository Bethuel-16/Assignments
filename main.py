# Import the array module
import array

# Creating an array of integers 'i' specifies the datatype
intarr = array.array('i', [1, 2, 3, 4, 5])

# Accessing elements
print(intarr[1])
# Appending an element
intarr.append(6)
# Removing an element
intarr.remove(3)
print(intarr)

import numpy as np
# Creating a NumPy array
np_array = np.array([1, 2, 3, 4, 5])
# Accessing elements
print(np_array[0])  # Output: 1
# Performing operations
np_array = np_array * 2  # Multiply each element by 2
print(np_array)  # Output: [2, 4, 6, 8, 10])
