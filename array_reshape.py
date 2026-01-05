import numpy as np

''' --- np.flatten --- '''
# Syntax: array_name.flatten(), Function: returns an array with one row 
# Note: Unlike ravel, flatten returns a new, independent array

# Define a 2D Array
k = np.array( [ [1, 2], [2, 1]])

# Flatten the 2D Array
print(f'Flattened Array: {k.flatten()}')


''' --- np.ravel --- '''
# Syntax: np.ravel(array_name), Function: returns an array with one row
# Note: Values of original array and array from np.ravel are connected (one changes other)

# Define a 2D Array
k = np.array( [ [1, 2], [2, 1]])

# Ravel the 2D Array
print(f'Raveled Array (1st Method): {np.ravel(k)}')
print(f'Raveled Array (2nd Method): {k.ravel()}')


''' --- np.reshape --- '''
'''Reshaping an Exisiting Array'''
# Syntax (1st Method): variable_name = np.reshape(array_name, (rows, columns))
# Syntax (2nd Method): variable_name = array_name.reshape( (rows, columns) )

# Define a 1D Array
o = np.arange(12)

# Reshape array into 3 rows of 4 columns
print(f'Reshaped Array (3, 4): \n{np.reshape(o, (3, 4))}') 

# Reshape array into 2 rows of 6 columns
print(f'Reshaped Array (2, 6): \n{o.reshape( (2, 6) )}') 

'''Separating an Array into Two Separate Arrays'''
# Syntax: variable_name = array_name.reshape(number_of_separate arrays, rows, columns)

# Reshape array into two separate arrays, each with 3 rows and 2 columns
print(f'Reshaped Array (2, 3, 2): \n{o.reshape(2, 3, 2)}') 

'''Special Case: -1 in np.reshape'''
# Explanation: -1 tells np.reshape() to use required # of columns/rows to fit all the elements
 
# Define a 1D Array
s = np.arange(10)  

# One row, however many columns needed to fit all the elements (10)
print(f'Reshaped Array with 1 Row: {s.reshape(1, -1)}') 

# One column, however many rows needed to fit all the elements (10)
print(f'Reshaped Array with 1 Column: {s.reshape(-1, 1)}') 

