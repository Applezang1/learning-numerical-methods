import numpy as np

''' --- Access 1D Array Elements --- '''
# Define 1D Array
A = np.array( [2, 4, 5])

# Access the 1st number of the array
print(f'1st Number: {A[0]}') 

# Change second element of array to 100
A[1] = 100  

# Print Modified Array 
print(f'Modified Array: {A}\n')


''' --- Access 2D Array Elements --- '''
# Define 2D Array
B = np.array( [ [2, 3, 5], [7, 11, 13] ] )

# Access the first row of the array 
print(f'First Row of Array: {B[0]}') 

# Access the second element in the first row
print(f'Second Element in First Row: {B[0][1]}') 

# Change the value of the third element in the second row to 999
B[1][2] = 999 

# Print Modified Array 
print(f'Modified Array: \n{B}')

# Note: Any array modifications affects ALL variables associated to that array
# Example: If two variables (A and B) are equal to the same array and B[1] = 3 occurs, A also experiences the same change