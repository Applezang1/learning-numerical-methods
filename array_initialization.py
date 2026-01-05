import numpy as np

''' --- np.ones ---'''
# One-dimensional array with three 1s (horizontal)
a = np.ones(3)
print(f'Ones (3, ): {a}\n')

# Two arrays of 1s with 3 rows and 4 columns
b = np.ones( (2, 3, 4) )
print(f'Ones (2, 3, 4):\n {b}\n')


''' --- np.zeros ---'''
# Array of 0s with 3 rows and 5 columns
a = np.zeros( (3,5) )
print(f'Zeros (3, 5):\n {a}\n') 

# Arrays of 0s 3 rows and 4 columns
b = np.zeros( (2, 3, 4) )
print(f'Zeros (2, 3, 4):\n {b}\n')


''' --- np.arange ---'''
# np.arange(start_value, end_value, increment) 
# Note: Stops when value is equal to or exceeds the end value 
f = np.arange(1, 10, 2) 
print(f'Output of np.arange: \n{f}\n') 


''' --- np.array ---'''
# One-dimensional array with the numbers in the square brackets
c = np.array([2.71, 3.14, 3000])
print(f'1D np_array: \n {c}\n') 

# Array of three rows each with one number in the square brackets
d = np.array([[2.71], [3.14], [3000]])
print(f'np_array (3, 1): \n {d}\n') 

# Array of two rows with 3 elements each 
e = np.array([[2, 3, 5], [7, 11, 13]])
print(f'np_array (2, 3): \n{e}\n') 


''' --- np.linspace ---'''
# np.linspace(start_value, end_value, num_points)
# Note: Array with 'num_points' equally spaced values from start_value to end_value (inclusive)
g = np.linspace(0, 10, 6)
print(f'Output of np.linspace: \n{g}\n')


