import numpy as np, matplotlib.pyplot as plt 

'''--- Brownian Motion Simulation ---'''
# Definition: The random movement of a particle over time periods 

'''Creating Random Number Generator Object'''
# Create a random number generator object 
rng = np.random.default_rng() 

# Assign its uniform distribution method to rand 
random = rng.random 
num_steps = 1000
num_points = 100

'''Define x-value trajectory'''
def generate_x_step():
    # Store 1000 random numbers between 0 - 1
    random_number1 = random(num_steps) 

    # If greater than 0.5, store it as true; otherwise, false
    # This implements random particle movement in Brownian motion
    x_step = random_number1 > 0.5 

    # Convert boolean array of true and false into 1 and -1
    x_value = x_step*2 - 1
    x_value = np.cumsum(x_value)
    return x_value

'''Define y-value trajectory'''
def generate_y_step():
    # Store 1000 random numbers between 0 - 1
    random_number2 = random(num_steps)

    # If greater than 0.5, store it as true; otherwise, false 
    # This implements random particle movement in Brownian motion
    y_step = random_number2 > 0.5 

    # Convert boolean array of true and false into 1 and -1
    y_value = y_step*2 - 1 
    y_value = np.cumsum(y_value)
    return y_value 

'''Store Final x and y Values and Displacement'''
x_final = np.zeros(num_points)
y_final = np.zeros(num_points)
displacement = np.zeros(num_points)
for i in range(num_points): 
    x_value = generate_x_step() 
    y_value = generate_y_step() 
    x_final[i] = x_value[-1]
    y_final[i] = y_value[-1]
    displacement[i] = np.sqrt(x_value[-1]**2 + y_value[-1]**2) 

'''Plotting'''
# Plot the change in x over the change in y
ax = plt.gca()
plt.scatter(x_final, y_final)
ax.set_xlabel("Change in X Value")
ax.set_ylabel("Change in Y Value")
ax.set_title("Scatter Plot of Brownian Motion")
plt.show() 

# Plot the histogram of the displacement
ax = plt.gca()
plt.hist(displacement)
ax.set_xlabel("Displacement Value")
ax.set_ylabel("Frequency")
ax.set_title("Histogram of Displacement from Brownian Motion")
plt.show() 

# Plot the histogram of the displacement^2
ax = plt.gca()
plt.hist(displacement**2)
ax.set_xlabel("Displacement Value")
ax.set_ylabel("Frequency")
ax.set_title("Histogram of Displacement^2 from Brownian Motion ")
plt.show()

# Compute the mean square displacement
mean_square_displacement = np.mean(displacement**2)
print(f"The mean square displacement is: {mean_square_displacement}")

# Visualize 4 subplots of the trajectory of brownian motion
num_sub_plots = 4
plt.figure()
for i in range(num_sub_plots):
    x_value = generate_x_step()
    y_value = generate_y_step()
    plt.subplot(2, 2, i+1); plt.plot(x_value, y_value)
    plt.axis('square')
plt.show()

