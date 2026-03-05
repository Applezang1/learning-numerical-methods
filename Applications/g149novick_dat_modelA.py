import numpy as np, matplotlib.pyplot as plt 

'''--- Beta Gal Experimental vs Model Data Comparison (Data: g149novickA.txt) ---'''
ax = plt.gca()

'''Experimental Data Plot'''
# Load data into an array
g149novickA = np.loadtxt('g149novickA.txt', delimiter = ',') 

# Define new array with time values
time2 = g149novickA[:, 0] 

# Define new array with experimental beta_gal_activity values
beta_gal_activity2 = g149novickA[:, 1] 

# Plot experimental beta_gal_activity over time values
plt.plot(time2, beta_gal_activity2) 

'''Model Data Plot'''
# Initialize an array of time values
time = np.linspace(0.1, 6.6, 10) 

# Define an experimental tao value
tao = 3.5 

# Define the model equation for beta_gal_activity
beta_gal_activity = 1 - np.exp(-time/tao) 

# Plot the model beta_gal_activity over time
plt.plot(time, beta_gal_activity) 

'''Plot Model and Experimental Data Plot'''
# Define line values
lines = ax.get_lines()
plt.setp(lines[0], linestyle = '--', linewidth = 2, color = 'r') # Experimental Data Line
plt.setp(lines[1], linestyle = '-', linewidth = 2, color = 'b') # Model Data Line

# Label data line and make a legend
lines[0].set_label('Experimental Data Line') # Label as Experimental Data Line
lines[1].set_label('Model A Data Line') # Label as Model Data Line
ax.legend()  

# Label x and y axis
ax.set_xlabel('Time (hours)')
ax.set_ylabel('Beta Galactosidase Activity')

# Make Title
ax.set_title("Change in Beta Galactosidase Activity over Time", size = 12, weight = 'bold')

# Show the plot
plt.show()

