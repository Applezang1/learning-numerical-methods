import numpy as np, matplotlib.pyplot as plt 

'''--- Basic Example of Plotting ---'''
# Define Plotting Variables
num_points = 5 
x_min, x_max = 0, 4 

# Define an array from 0 to 4 with 5 points as the input array
x_values = np.linspace(x_min, x_max, num_points) 

# Compute the output array (x^2)
y_values = x_values**2 

# Validate whether the input and output array's shapes align
assert len(x_values) == len(y_values), "Length-mismatch: {:d} versus {:d}".format(len(x_values), len(y_values)) 

# Plot the Graph
plt.plot(x_values, y_values) 

# Obtain Figure, Axes, and Line Object
ax = plt.gca() 
lines = ax.get_lines() 

# Update the line properties and label the line
plt.setp(lines[0], linewidth = 5, color = 'r') 
lines[0].set_label("Line") 

# Add a Title
plt.title("Plot of 5 Points", size = 20, weight = 'bold') 

# Add the x and y label
plt.xlabel("x values") 
plt.ylabel("y values") 

# Define a legend
ax.legend()

# Show the plot
plt.show() 

