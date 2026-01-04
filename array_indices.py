import numpy as np 

''' --- Lists and Arrays as Indicies --- '''
# Define a 1D Array
t = np.arange(10, 21)

# Define Indices
u = [2, 4, 5] 

# Make an array of the 3rd, 5th, and 6th element
print(f'Array of 3rd, 5th, 6th: {t[u]}') 


''' --- Using Boolean array to select entries from another array of the same shape --- '''
# Define a 1D Array
v = np.arange(-10, 11) 

# Define a Boolean Array
# Values less than 5 are stored as True and values greater than 5 are stored as False
less_than_five = (abs(v) < 5) 

# Include elements that were True in a new array
print(f'Boolean Filtered Array: {v[less_than_five]}') 

