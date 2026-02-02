from scipy.optimize import fsolve 
import numpy as np, matplotlib.pyplot as plt

'''--- Complex Roots (np.roots) ---'''
# The following function returns two real roots, despite it having 4 roots
def f(x): return x * (1+x**3) - 1

# Print two real roots
print(f'First real root: {fsolve(f, 1)}')
print(f'Second real root: {fsolve(f, -1)}') 

# Use np.roots to find complex roots
print(np.roots([1, 0, 0, 1, -1])) 


'''--- Complex Nonlinear Equations (fsolve) ---'''
# Define a function that allows for the computation of complex roots
def f(x): 
    z = x[0] + 1j*x[1] # Lets fsolve plug in complex roots as well
    q = 1/z -1 -z**2.4 # Plug in complex roots/roots to equation
    return q.real, q.imag 

# Find real root 
print(f'Real root: {fsolve(f, [2, 0])}')

# Find first complex root 
print(f'First complex root: {fsolve(f, [0, 2])}') 

# Find second complex root 
print(f'Second complex root: {fsolve(f, [0, -2])}')


'''--- Finding Roots of Any Polynomial (fsolve) ---'''
'''Example 1 (x^2-1)'''
# Define polynomial: x^2 -1
def f(x): return x**2 -1 

# Solve for the root closest to 0.5
print(f'Root closest to 0.5: {fsolve(f, 0.5)}') 

# Solve for the root closest to -0.5
print(f'Root closest to -0.5: {fsolve(f, -0.5)}') 

# Solve for roots found near -0.5 and 0.5
print(f'Root(s) near -0.5 and 0.5: {fsolve(f, [-0.5, 0.5])}')

'''Example 2 (sin(x)^10)'''
# Define polynomial: sin(x)^10
def f(x): return np.sin(x)**10

# Solve for the root closest to 1 for sin(x)
print(f'Root closest to 1 for sin(x): {fsolve(np.sin, 1)}')

# Solve for the root closest to 1 for sin(x)^10
print(f'Root closest to 1 for sin(x)^10: {fsolve(f, 1)}')

'''Example 3 (1/(x-1))'''
# Define Polynomial: 1/(x-1)
def f(x): return 1/(x-1) 

# Solve for the root closest to 2
print(fsolve(f, 2)) 

