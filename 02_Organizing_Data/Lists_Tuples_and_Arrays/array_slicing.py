import numpy as np

''' --- Slicing 1D Array Elements --- '''
# Slicing Syntax: variable_name[start:end:stride] 
# Define a 1D Array
j = np.arange(1, 21, 1)

# Print all elements in the array
print(f'All Elements: {j[:]}') 

# Start at 5, print rest of elements after 5 in the array
print(f'Every Element after 5: {j[5::]}') 

# Start at 0, print all integers before 5
print(f'Every Element up to 5 from 0: {j[:5:]}') 

# Start at 0, print all integers in increments of 5
print(f'Every 5th Element from 0: {j[::5]}') 


''' --- Slicing 2D Array Elements --- '''
# Slicing Syntax: variable_name[row_start: row_end, col_start: col_end]
# Define a 2D Array
C = np.array( [[1, 2, 3], [4, 5, 6], [7, 8, 9]])  

# Print first row, all columns
print(f'All Columns of First Row: {C[0, :]}') 

# Print all rows, second column
print(f'All Rows of Second Column: {C[:, 1]}') 

# Print first two rows, last two columns
print(f'Last Two Columns of First Two Rows: \n{C[0:2, 1:3]}') 

# Print second row down, first two columns
print(f'First Two Columns of Last Two Rows: \n{C[1:, :2]}') 

# Print last row
print(f'Last Row: {C[-1, :]}') 

# Note: Array Slices can be used to replace section with another value 
# Example: A[0:3] = np.ones(3)