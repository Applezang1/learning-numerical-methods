import numpy as np, matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # 3D plotting tool 
from numpy.random import random as rand, random

'''--- 3D Graphs ---'''
# Create a new figure
fig = plt.figure() 

# Create 3D plotter attached to figure
ax = fig.add_subplot(111, projection='3d') 

# Define parameter for parametric plot
t = np.linspace(0, 5*np.pi, 501) 

# Plot 3D plot
ax.plot(np.cos(t), np.sin(t), t) 
plt.show() 


'''--- Multiple Plots ---'''
# Definition: Creating several curves on the same axes

# Method 1: Input more than one (x,y) pair
# Define Plotting Variables
x = np.linspace(0, 1, 51)
y1 = np.exp(x)
y2 = x**2 

# Graph Multiple Plots
plt.plot(x, y1, 'r', x, y2, 'ko') 
plt.show()

# Method 2: Define y as a two-dimensional array: 
# Define Plotting Variables
num_curves = 3 
x = np.linspace(0, 1, 51)
y = np.zeros( (x.size, num_curves))
for n in range(num_curves): 
    y[:, n] = np.sin((n+1) * x * 2 * np.pi) 

# Graph Multiple Plots
plt.plot(x, y)


'''--- Multiple Plot Windows ---'''
# Create a new figure and make it the "active" figure
plt.figure('joe') 

# Generate second plot in new figure
plt.plot() 

# Close plot
plt.close() 


'''--- Subplot ---'''
# Method 1 for Subplots
# Syntax: plt.subplot(M, N, p): figure with M rows and N columns and p (location of plot)
t = np.linspace(0, 1, 101)
plt.figure()
plt.subplot(2, 2, 1); plt.hist(random(20)) # Upper Left
plt.title("Data") # Title for Upper Left
plt.subplot(2, 2, 2); plt.plot(t, t**2, t, t**3 - t) # Upper Right
plt.title("Functions") # Title for Upper Right
plt.subplot(2, 2, 3); plt.plot(random(20), random(20), 'r*') # Lower Left
plt.subplot(2, 2, 4); plt.plot(t*np.cos(10*t), t*np.sin(10*t)) # Lower Right
plt.suptitle("Data and Functions") # Overall Title
plt.show() 

# Method 2 for Subplots
t = np.linspace(0, 1, 101)
fig, ax = plt.subplots(2, 2) # Creates a 2x2 grid of subplots
ax[0,0].hist(random(20)) # Access subplot in coordinates (0, 0)
ax[0,1].plot(t, t**2, t, t**3 - t)
ax[1,0].plot(random(20), random(20), "r*")
ax[1,1].plot(t*np.cos(10*t), t*np.sin(10*t))
fig.suptitle("Data and Functions") # Overall Title
plt.show()


'''--- Bar Graphs ---'''
# Syntax: plt.bar(array of bar positions, array of bar heights, single width/array of width for the rectangles)
# Important: Bar Graphs need the count (# in each bar) and bin_edges from plt.hist
# Define Bar Plotting Variables
data = rand(100)
counts, bin_edges, _ = plt.hist(data) # Counts: y_value, Bin_edges: x_values

'''Example 1:'''
# Compute distance between bin edges
bin_size = bin_edges[1] - bin_edges[0] 

# Compute the width of the bar
new_widths = bin_size * counts / counts.max() 

# Plot the Bar Graph
# Note: Slice bin_edges to align 11 edges with 10 counts
plt.bar(bin_edges[:-1], counts, width = new_widths, color=['r', 'g', 'b']) 
plt.show() 

'''Example 2:'''
plt.bar(bin_edges[:-1], counts, width = bin_size, align = 'edge') 
plt.show()


'''--- Histogram ---'''
# Syntax: plt.hist can take keyword argument bins = (Name # of bins you want)
# Syntax: Also takes align = 'mid' (How bars are alligned relative to bin) 

'''Example 1:'''
# Define Plotting Variable
data = rand(100)
counts, bin_edges, _ = plt.hist(data) # Counts: y_value, Bin_edges: x_values
print(f'y_value of each bar: {counts}') # Array #1: y-value of each bar
print(f'Bin edge values: {bin_edges}') # Array #2: Bin edge values
plt.show() 

'''Example 2:'''
# Define an array with inverse powers of 2
log2bins = np.logspace(-8, 0, num=9, base=2)

# Set first element of array to 0
log2bins[0] = 0.0 

# Plot a histogram
plt.hist(data, bins=log2bins) 
plt.show()


'''=== Graphs for Functions with Two Independent Variables h(x,y) ==='''
'''--- Contour Plot ---'''
# Definition: two-dimensional drawing where contour lines are used to represent the height (topographic map)

# Define Plotting Variables
x_vals = np.linspace(-3, 3, 21) 
y_vals = np.linspace(0, 10, 11)

# Make 2 arrays of all the combinations of x and y values
X, Y = np.meshgrid(x_vals, y_vals) 

# Compute the output of a function with two independent variables
Z = np.cos(X) * np.sin(Y) 

# Plot the contour plot, where 20 represents the number of contour lines
cs = plt.contour(X, Y, Z, 20, linewidths = 3)
plt.clabel(cs, fontsize = 5) # Label each contour line 
plt.colorbar(cs) # Add color bar to represent color as y-value
plt.show()


'''--- Filled Contour Plot ---'''
# Plot the filled contour plot, where spaces between the lines are filled
cs = plt.contourf(X, Y, Z, 20, linewidth = 3)
plt.colorbar(cs)
plt.show() 


'''--- Heat Map ---'''
# Definition: uses color to indicate height
# Define Plotting Variables
x_vals = np.linspace(-3, 3, 21) 
y_vals = np.linspace(0, 10, 11) 

# Makes 2 arrays of all combinations of x and y values
X, Y = np.meshgrid(x_vals, y_vals) 

# Compute the output of a function with two independent variables
Z = np.cos(X) * np.sin(Y) 

# Plot the heatmap with shading for better graph visuals
heatmap = plt.pcolormesh(X, Y, Z, shading = 'gouraud') 
plt.colorbar(heatmap)
plt.show()


'''--- Streamlines ---'''
# Definition: Smooth lines showing vector movement
# Define Plotting Variables
lower, upper, step = -2, 2, 0.1 
coords = np.arange(lower, upper + step, step)

# Compute all combinations of X and Y
X, Y = np.meshgrid(coords, coords)

# Assign Vectors to make a Circular Vector Field
Vx, Vy = X, -Y

# Plot Streamline
plt.streamplot(X, Y, Vx, Vy, linewidth = 2)
plt.axis('square')
plt.show()


'''--- Vector Fields ---'''
# Define Plotting Variables
coords = np.linspace(-1, 1, 11)

# Compute all combinations of X and Y
X, Y = np.meshgrid(coords, coords)

# Assign Vectors to make a Circular Vector Field
Vx, Vy = Y, -X 

# Plot Vector Field
plt.quiver(X, Y, Vx, Vy, pivot = 'mid', angles = 'xy')
plt.axis('square')
plt.show() 


'''--- Gradient Vector Field ---''' 
# Define Plotting Variables
skip = 5
coords = np.linspace(-2, 2, 101) 

# Define a Coarse grid for gradient using every 5th point
X, Y = np.meshgrid(coords[::skip], coords[::skip]) 

# Calculate Distance using Distance Formula (coarse grid)
R = np.sqrt(X**2 + Y**2)

# Compute the 2D Gaussian Hill (coarse grid)
Z = np.exp(-R**2)

# Define a Fine grid for gradient 
x, y = np.meshgrid(coords, coords) 

# Calculate Distance using Distance Formula (fine grid)
r = np.sqrt(x**2 + y**2) 

# Compute the 2D Gaussian Hill (fine grid)
z = np.exp(-r**2)

# Finds spacing between points
ds = coords[skip] - coords[0] 

# Calculates partial derivatives to see how Z changes at every point
dX, dY = np.gradient(Z, ds) 

# Plot the Gradient Vector Field
plt.contourf(x, y, z, 25)
plt.set_cmap('coolwarm')
plt.quiver(X, Y, dX.T, dY.T, scale = 25, angles = 'xy', color = 'k')
plt.axis('equal')
plt.show()