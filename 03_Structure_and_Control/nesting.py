import numpy as np

''' --- Nesting --- '''
# Definition: Embeding a loop inside of another loop'''

'''Example of Nesting'''
# Define Variables
rows, columns = 3, 4
p, q = 0.1, 0.3

# Define an array structure of zeros
A = np.zeros( (rows, columns))

# Run Nesting Loop
for m in range(rows): 
    for n in range(columns): 
        A[m, n] = p**m * q**n

# Print Results 
print(f'Resulting Array: \n{A}')