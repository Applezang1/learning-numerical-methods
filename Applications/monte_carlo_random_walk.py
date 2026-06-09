import numpy as np, matplotlib.pyplot as plt

'''--- Computing the Number of Heads in # of Flips---'''
# Create a random number generator object
rng = np.random.default_rng() 

# Assign its uniform distribution method to rand (returns a random number)
rand = rng.random(100) 

# Store it in an array
samples = np.array((rand), dtype = 'float') 

# Values less than 0.5 are counted as heads
flips = samples<0.5 

# Count the number of heads 
print(f"The number of heads was {np.sum(flips)}") 


'''--- Monte Carlo Simulation (Random Steps) ---'''
'''Final Coordinate of a Person after # of Steps'''
# Define the number of steps
num_steps = 500

# Define a function to compute the final coordinate of a person after # of steps'''
def get_coordinate(num_steps): 
    '''X-values'''
    # Random Number Generator Object
    rng = np.random.default_rng() 

    # Makes num_steps amount of random numbers
    x_rand = rng.random(num_steps) 

    # Stores it in an array
    x_steps = np.array((x_rand), dtype = 'float') 

    # Values greater than 0.5 are a step by 1 unit 
    positive_x = x_steps > 0.5 

    # Positive steps - negative steps = resulting steps
    x_step = np.sum(positive_x) - (num_steps - np.sum(positive_x)) 

    '''Y-values'''
    y_rand = rng.random(num_steps)
    y_steps = np.array((y_rand), dtype = 'float') 
    positive_y = y_steps > 0.5  
    y_step = np.sum(positive_y) -  (num_steps - np.sum(positive_y)) 
    
    return x_step, y_step

# Compute and print the final coordinate of a person after 500 steps
x_coordinate, y_coordinate = get_coordinate(500)
print(f"This person is at ({x_coordinate}, {y_coordinate})")

'''Trajectory of Person during # of Steps'''
# Define a function to compute the trajectory of a person during # of steps'''
def trajectory(num_steps):
    rng = np.random.default_rng() 
    rand = rng.random(num_steps) # Random values from 0-1 
    rand2 = rng.random(num_steps)

    '''X-values'''
    # Boolean Array of True and False for x-values
    x_values = rand > 0.5 

    # Converts True to +1, False to -1 for x-values
    x_step = 2* x_values - 1 

     # Array of x_position over time
    x_position = np.cumsum(x_step)

    '''Y-values'''
    # Boolean Array of True and False for y-values
    y_values = rand2 > 0.5 

    # Converts True to +1, False to -1 for y-values 
    y_step = 2* y_values - 1 

    # Array of y_position over time
    y_position = np.cumsum(y_step) 

    return x_position, y_position

'''Plotting'''
# Define the number of subplots for the graph
M, N = 2, 2 

# Loop over each subplot and plot the trajectory
for i in range(1, 5): 
    x_position, y_position = trajectory(num_steps)
    plt.subplot(M, N, i); plt.plot(x_position, y_position)
    plt.axis('square')

plt.suptitle("Plot of Individual's Position over Time")
plt.show()










