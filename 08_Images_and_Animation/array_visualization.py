import numpy as np
import matplotlib.pyplot as plt

'''--- Arrays to Images (plt.imshow) ---'''
# Function of plt.imshow: Display an image from an array of numbers
# Key Information: Array indices are [y, x] while Cartesian is [x, y] 
# Transpose or use origin = 'lower' is used to flip array indices to [x, y]

'''Example 1:'''
# Define an array structure of zeros
M = np.zeros((40, 40))

# Fill the array structure with random values
M[:10, :10] = np.random.random((10, 10))
M[10:, 10:] = np.random.random((30, 30))

# Display the array as image
plt.imshow(M, origin = 'lower')
plt.colorbar()
plt.show() 

'''Example 2:'''
# Define a coordinate grid.
x_max, y_max = 2, 1
x_num, y_num = 200, 100

# Define an array of values for x-values and y-values
x = np.linspace(0, x_max, x_num)
y = np.linspace(0, y_max, y_num)

'''Combine x-values and y-values into an array ('z') of the two combinations'''
# Method 1: Initialize z-values using a loop
z = np.zeros((y_num, x_num))
for i in range(x_num):
    for j in range(y_num):
        z[j, i] = (x[i] - 2 * y[j])**2

# Method 2: Initialize z-values using np.meshgrid
X, Y = np.meshgrid(x, y)
Z = (X - 2 * Y)**2

'''Plotting'''
# Plots the x-values and y-values using different methods
fig, ax = plt.subplots(2, 3, figsize=(14, 7))
fig.suptitle(r"Plots of $f(x, y) = (x-2y)^2$")

# Method 1: Image Coordinates [(0, 0) at top left]
ax[0, 0].imshow(z)
ax[0, 0].set_title("Loop: Image Coordinates")

# Method 2: Spatial Coordinates [(0, 0) at bottom left]
ax[0, 1].imshow(z, origin='lower')
ax[0, 1].set_title("Loop: Spatial Coordinates")

# Method 3: Meshgrid Image Coordinates
ax[0, 2].imshow(Z)
ax[0, 2].set_title("meshgrid: Image Coordinates")

# Method 4: Swaps rows and columns of Spatial Coordinates
ax[1, 0].imshow(z.T, origin='lower') 
ax[1, 0].set_title("Loop: Transpose + Spatial Coordinates")

# Method 5: Meshgrid Spatial Coordinates
ax[1, 1].imshow(Z, origin='lower')
ax[1, 1].set_title("meshgrid: Spatial Coordinates")

# Method 6: Colormesh of x-values and y-values with colors corresponding to function output
c = ax[1, 2].pcolormesh(X, Y, Z, shading='auto')
ax[1, 2].set_aspect('auto')
ax[1, 2].set_title("pcolormesh")
fig.colorbar(c, ax=ax[1, 2])

plt.tight_layout()
plt.show()