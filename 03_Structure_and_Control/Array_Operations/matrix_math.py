import numpy as np

''' --- Matrix Math and Operations --- '''
# Define Arrays
a = np.array( [1, 2, 3])
b = np.array ( [1, 0.1, 0.01] )

# Compute the Dot Product and Element-Wise Multiplication of Arrays
print(f'Element-Wise Multiplication: {a*b}') 
print(f'Dot Product: {np.dot(a,b)}') 

''' Combine Broadcasting with Matrix Math '''
# Broadcast Arrays for Matrix Math
a = np.array ( [1, 2, 3] ).reshape((3, 1))
b = np.array ( [1, 0.1, 0.01] ).reshape((1, 3))

print(f'Result of Broadcasting Array A: \n{a}')
print(f'Result of Broadcasting Array B: {b}')

# Compute the Dot Product of the Arrays
print(f'Broadcasted Element-Wise Multiplication:\n {a*b}')
print(f'Broadcasted Dot Product:\n {np.dot(a,b)}')
