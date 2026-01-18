import numpy as np
from scipy.special import factorial

''' --- Boolean Vectorizing --- '''
# Definition: Performing operations with boolean arrays

# Define Boolean Arrays
x = np.array([True, True, False, False])
y = np.array([True, False, True, False])

# Apply logical OR to each element
print(f'Logical OR (|): {x | y}') 

# Apply logical AND to each element
print(f'Logical AND (&): {x & y}') 

# Apply logical NOT to each element 
print(f'Logical NOT (~): {~x}') 


''' --- Broadcasting --- '''
# Definintion: Arrays are stretched/broadcasted in order to be addable

# Example: b is broadcasted to...
# ([10, 20, 30])
# ([10, 20, 30]) 
# In order to be able to be added with array a

# Define Arrays
a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([10, 20, 30])

# Add Arrays
print(f'Broadcasting Output: \n{a + b}')  


''' --- Vectorizing --- '''
# Definition: Using arrays for math instead of for or while loops

# Define Variables
b, c = 2, -1  
a = np.arange(1, 2, 0.3)

'''Example 1'''
# Example 1: Solutions to Quadratic Formula
print(f'Array of Solutions to Quadratic Formula: \n{(-b + np.sqrt(b**2 - 4*a*c))/ (2*a)}') 

'''Example 2'''
# Define Array
z = np.arange(1, 10, 1)

# Example 2: Gaussian/Exponential Function
print(f'Outputs of Exponential: \n{np.e**-z**2}') 

'''Example 3'''
# Define Variables
N, y = 10, 2
n_array = np.arange(0, N + 1, 1)

# Example 3: Poisson Distribution
print(f'Output of Poisson Distribution: \n{((np.e**-y)* 2**n_array)/factorial(n_array)}')  