from scipy.integrate import quad 
import numpy as np, matplotlib.pyplot as plt

'''--- Integration (quad) ---''' 
# Function: quad returns the result of integral and estimate of error
# Define input array for upper limit of integration
x_max = np.linspace(0, 3*np.pi, 16)

# Define array structure to store integration results
integral = np.zeros(x_max.size) 
for i in range(x_max.size): 
    # Evaluate the integral of cosine with a lower limit of 0 to a upper limit of x_max
    integral[i], error = quad(np.cos, 0, x_max[i])

# Plot the graph of the integral 
plt.plot(x_max, integral) 
plt.show() 

# Print the integration of cosine with an upper limit of 5000, with 1000 maximum subintervals
print(f"Integration for cosine: {quad(np.cos, 0, 5000, limit=1000)}") 
print(f"Real Value for the integration of cosine {np.sin(5000)}")

'''Method 1 of Integration'''
# Method #1: Use Dummy Function
# Define a function of several variables
def f(x, a, b, c): return a*x**2 + b*x + c  

# Assign constant values to a, b, c and keep 'x' a variable
def g(x): return f(x, 1, 2, 3) 

# Compute the integral with lower limit of -1 and upper limit of 1 for 'x'
integral1, err = quad(g, -1, 1)

'''Method 2 of Integration'''
# Method 2: Use Keyword 
integral2, err = quad(f, -1, 1, args=(1, 2, 3)) # Set a, b, c as 1, 2, 3 


'''--- Integration Examples ---'''
'''Example 1: Integral of the function x^2'''
# Define Function
def f(x): return x**2 

# Define upper limits of integration
x_max = np.linspace(0, 2, 10)

# Define array structure for integral results
integral = np.zeros(x_max.size) 

# Compute the integral over all upper limits of integration
for i in range(x_max.size): 
    integral[i], error = quad(f, 0, x_max[i]) 

# Plot the integral results over upper limits of integration
plt.plot(x_max, integral)
plt.show() 

'''Example 2: Integral of the function e^([-x^2]/2)'''
# Define Function
def f(x): return np.exp(-x**2/2) 

# Define upper limits of integration
x_max = np.linspace(0, 5, 20)

# Define array structure for integral results
integral = np.zeros(x_max.size)

# Compute the integral over all upper limits of integration
for i in range(x_max.size):
    integral[i], error = quad(f, 0, x_max[i])

# Plot the integral results over upper limits of integration
plt.plot(x_max, integral)
plt.show() 

'''Example 3: Integral of the function e^([-x^2]/2) over infinite limits'''
# Define Function
def f(x): return np.exp(-x**2/2) 

# Compute the integral over infinite limits
integral, error = quad(f, -np.inf, np.inf)
print("Difference from exact result: ", integral - np.sqrt(2*np.pi))