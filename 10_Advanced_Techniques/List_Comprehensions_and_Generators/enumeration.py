'''--- Enumeration ---'''
import numpy as np, matplotlib.pyplot as plt
# Definition: Enumeration gives an order for the elements of a collection as you access them 

'''Example #1:'''
# Define a list of values
L = [n**2 for n in range(10)] 

# Enumerate the list over its values to include the order of the elements in the list
for x in enumerate(L): 
    print(x)

'''Example #2:''' 
# Define an array of theta values
theta = np.linspace(-2*np.pi, 2*np.pi, 201)

# Define four separate functions for plotting
functions = { r"$\sin \theta$": np.sin(theta), 
              r"$\sin^2 \theta$": np.sin(theta)**2, 
              r"$\cos \theta$": np.cos(theta), 
              r"$\cos^2 \theta$": np.cos(theta)**2 }

# Define line styles
styles = ['r-', 'g--', 'b:', 'k-.']

# Use enumeration to assign different line styles to graphs of different functions for plotting
plt.figure()
for n, k in enumerate(functions.keys()): 
    plt.plot(theta, functions[k], styles[n], label=k)
plt.legend() 
plt.show()

# Use enumeration to assign different subplots to graphs of different functions
fig, ax = plt.subplots(2, 2, sharex = True, sharey = True)
for n, k in enumerate(functions.keys()): 
    I, J = n // 2, n % 2 # Use modular arithmetic to get subplot indices 
    ax[I, J].plot(theta, functions[k])
    ax[I, J].set_title(k) 
plt.show()


'''--- np.ndenumerate ---'''
# Function: Returns the index value and the actual value of each value/point
# Example:
the_shape = (4,4)

# Assign random values to a 4 x 4 shape
R = np.random.random(the_shape)

# Use np.ndenumerate to compute the value assigned to each index
for I, r in np.ndenumerate(R): 
    print("The element at {} is {:.3f}.".format(I, r))


'''--- np.ndindex ---'''
# Function: Returns the index value of each value/point
# Example:
# Assign two sets of random values to a 4 x 4 shape
R1 = np.random.random(the_shape)
R2 = np.random.random(the_shape)

# Use np.ndindex to return the index value of each point in the 4 x 4 shape
for I in np.ndindex(the_shape): 
    print("The elements are {} are {:.3f} and {:.3f}.".format(I, R1[I], R2[I]))