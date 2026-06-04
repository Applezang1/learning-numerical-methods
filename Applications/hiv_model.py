import numpy as np, matplotlib.pyplot as plt

'''--- HIV Viral Load Experimental vs Model Data Comparison (Data: HIVseries.csv) ---'''
'''Model Data Plot'''
# Define an array of time values
time = np.linspace(0, 7, 11)

# Initialize parameter values
B = 0.12e+05 # Initial viral load component
A = 93240 # Primary viral load component
alpha = 0.333 # Rapid decay rate (first phase)
beta = 0.456 # Slower decay rate (second phase)

# Define the model equation for viral load
viral_load = A * np.exp(-alpha*time) + B * np.exp(-beta*time)

# Plot the model viral load over time values
plt.plot(time, viral_load)

'''Experimental Data Plot'''
# Load the experimental values of viral load
hiv_data = np.loadtxt('HIVseries.csv', delimiter = ',') 

# Define an array of time values
time = hiv_data[:, 0]

# Define an array of experimental viral load values
viral_load = hiv_data[:, 1]

# Plot the experimental viral load over time values
plt.plot(time, viral_load)
plt.show()