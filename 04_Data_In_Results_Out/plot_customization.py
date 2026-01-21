import numpy as np, matplotlib.pyplot as plt  

'''--- Customization for Axes Plot Visualization --- '''
plt.xlim(1, 6) # Change the range for x-axis 
plt.ylim(1, 6) # Change the range for y-axis 
plt.axis('tight') # Make the axis barely fit the range of data 
plt.axis('equal') # Same scaling of x and y 
plt.axis('square') # Graph is square in shape 
plt.scatter() # Draws points without connecting the lines 

'''--- Customization for Logarithmic Axes ---'''
plt.semilogy() # Logarithmic y-axis
plt.semilogx() # Logarithmic x-axis
plt.loglog() # Log-Log plot

'''--- Example of Logarithmic Axes ---'''
# Define Plotting Variables
num_points = 10 
x_min = 2
x_max = 7 
x_values = np.linspace(x_min, x_max, num_points)

# Compute the y-values of x^3.6
y_values = x_values**3.6

# Compute the y-values of e^x
y2_values = np.exp(x_values)

# Plot x^3.6
plt.plot(x_values, y_values, 'r')

# Plot e^x
plt.plot(x_values, y2_values, 'b') 
plt.show() 

# Plot x^3.6 using semilog plot
plt.semilogy(x_values, y_values, 'r') 

# Plot e^x using semilog plot
plt.semilogy(x_values, y2_values, 'b') 
plt.show()  

# Plot x^3.6 using log-log plot
plt.loglog(x_values, y_values, 'r') 

# Plot e^x using log-log plot
plt.loglog(x_values, y2_values, 'b') 
plt.show()