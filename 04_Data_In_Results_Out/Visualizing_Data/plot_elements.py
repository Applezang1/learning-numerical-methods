import numpy as np, matplotlib.pyplot as plt 

# Define Plotting Variables
num_points = 5 
x_min, x_max = 0, 4 
x_values = np.linspace(x_min, x_max, num_points) 
y_values = x_values**2 

# Validate whether the input and output arrays are the same length
assert len(x_values) == len(y_values), "Length-mismatch: {:d} versus {:d}".format(len(x_values), len(y_values))

# Plot the graph
plt.plot(x_values, y_values)

'''--- Axis Labels ---'''
# Get current axis and returns modifiable plot information
ax = plt.gca()

# Axis Labels Method 1
ax.set_xlabel('speed')
ax.set_ylabel('kinetic energy')

# Axis Labels Method 2
plt.xlabel('speed')
plt.ylabel('kinetic energy')

'''--- Error Bars ---''' 
# Define Error Bar Distance
x_errors, y_errors = 1, 2

# Define a new line with error bars extending by distance x/y_errors
# Note: fmt specifies marker 
plt.errorbar(x_values, y_values, yerr = y_errors, xerr = x_errors, fmt = 'or')

'''--- Legends and Labels ---'''
# Use "label" keyword to set labels when plotting 
plt.plot(x_values, y_values, label = 'Population 1')
plt.plot(x_values, x_values**3, label = 'Population 2')

# Display the legend in plot 
plt.legend() 

# Use line objects to set labels after plotting
ax = plt.gca() 
lines = ax.get_lines() 
lines[0].set_label("Infected Population")
lines[1].set_label("Cured Population")
ax.legend() 

'''--- Line Style ---'''
# Get access to list of line objects 
lines = ax.get_lines() 

# Define line[0] to be a thick, dashed, red line
plt.setp(lines[0], linestyle = '--', linewidth = 3, color = 'r') 

'''--- Text Boxes ---'''
# Define Variables for Text Boxes 
slope, intercept = 4, 1

# Write the slope-intercept equation at (2, 3)
plt.text(2, 3, "y = {:.3f} x + {:.3f}".format(slope, intercept)) 

'''--- Tick Labels ---'''
# Change the font and size of numbers that are labeling tick marks 
ax.set_xticklabels(ax.get_xticks(), family = 'monospace', fontsize = 10)
ax.set_yticklabels(ax.get_yticks(), family = 'monospace', fontsize = 10) 

'''--- Title ---'''
# Set a title with modifiable text parameters
ax.set_title("My first plot", size=24, weight='bold') 
plt.title("My first plot", size=24, weight='bold') 
plt.show()

'''--- Optional Parameters for Plot ---'''
# Color: 'r' (red), 'b' (blue), ... 
# Data Point Line: ':' (dotted line), '--' (dashed line), '-' (solid line) 
# Data Point Dots: '.' (small dot), 'o' (larger dot) 
