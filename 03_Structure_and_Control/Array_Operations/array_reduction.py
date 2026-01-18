import numpy as np

''' --- np.sum --- '''
# Function: A type of reducing function, which combines elements of the array with operations
# Syntax: np.sum(array, axis)

# Define a 2D Array
a = np.vstack( (np.arange(20), np.arange(100, 120) )) 

# 0: Sum by columns
print(f'Sum by Columns: {np.sum(a, 0)}') 

# 1: Sum by rows
print(f'Sum by Rows: {np.sum(a, 1)}') 

# No Axis: Sum all the array's elements
print(f'Sum all Elements: {np.sum(a)}') 


