import numpy as np, matplotlib.pyplot as plt 

'''--- Plotting Outputs of the Model Equation for Different Parameters---'''
'''First Set of Parameter Values'''
# Define parameter values
A = 1
tao = 1 

# Define an array of time values
time = np.linspace(0, 2, 10)

# Define the model equation for beta_gal_activity
beta_gal_activity = A*(np.exp(-time/tao)-1+(time/tao)) 

# Plot the model beta_gal_activity over time values 
plt.plot(time, beta_gal_activity) 

# Update line format
ax = plt.gca()
lines = ax.get_lines()
plt.setp(lines[0], linestyle = '--', linewidth = 3, color = 'r')

'''Second Set of Parameter Values'''
# Define parameter values
A = 10
tao = 3 

# Define an array of time values
time = np.linspace(0, 2, 10)

# Define the model equation for beta_gal_activity
beta_gal_activity = A*(np.exp(-time/tao)-1+(time/tao)) 

# Plot the model beta_gal_activity over time values
plt.plot(time, beta_gal_activity) 

# Update line format
lines = ax.get_lines()
plt.setp(lines[1], linestyle = '-', linewidth = 3, color = 'b')

'''Third Set of Parameter Values'''
# Define parameter values
A = 0.1
tao = 2.3 

# Define an array of time values
time = np.linspace(0, 2, 10)

# Define the model equation for beta_gal_activity
beta_gal_activity = A*(np.exp(-time/tao)-1+(time/tao)) 

# Plot the model beta_gal_activity over time values
plt.plot(time, beta_gal_activity) 

# Update line format
lines = ax.get_lines()
plt.setp(lines[2], linestyle = ':', linewidth = 3, color = 'g')

# Make and label each of the lines and make a legend
lines[0].set_label("A:1, tao: 1")
lines[1].set_label("A:10, tao: 3")
lines[2].set_label("A:0.1, tao: 2.3")
ax.legend()

plt.show()