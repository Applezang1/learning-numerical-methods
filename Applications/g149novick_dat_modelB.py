import numpy as np, matplotlib.pyplot as plt 

'''--- Beta Gal Experimental vs Model Data Comparison (Data: g149novickB.txt) ---'''
ax = plt.gca()

'''Experimental Data Plot'''
# Load data into an array
g149novickB = np.loadtxt('g149novickB.txt', delimiter = ',') 

# Define a new array with time values less than 10 hours
time2 = g149novickB[:16, 0]

# Define a new array with beta_gal_activity values
beta_gal_activity2 = g149novickB[:16, 1] 

# Plot the experimental beta_gal_activity over time
plt.plot(time2, beta_gal_activity2) 

'''Model Data Plot'''
# Define an array of time values
time = np.linspace(0, 10, 10)

# Initialize experimental values
A = 500 
tao = 1300 

# Define the model equation for predicting beta_gal_activity
beta_gal_activity = A*(np.exp(-time/tao)-1+(time/tao)) 

# Plot the model beta_gal_activity over time
plt.plot(time, beta_gal_activity) # Plot

'''Plotting'''
# Define line values
lines = ax.get_lines()
plt.setp(lines[0], linestyle = '--', linewidth = 2, color = 'r') # Experimental Data Line
plt.setp(lines[1], linestyle = '-', linewidth = 2, color = 'b') # Model Equation Line 

# Make a Legend 
lines[0].set_label("Experimental Data Line")
lines[1].set_label("Model B Line")
ax.legend() 

# Label x and y axis
ax.set_xlabel("Time (hours)")
ax.set_ylabel("Beta Galactosidase Activity")

# Make a Title
ax.set_title("Change in Beta Galactosidase Activity over Time", size = 12, weight = 'bold')

# Show plot
plt.show()
