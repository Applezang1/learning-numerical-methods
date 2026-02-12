import numpy as np, matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation 

'''--- Movie of the steps of a two-dimensional random walk ---'''
# Animation Common Design Principle 
# 1) Create an empty plot
# 2) Take control of the line of point objects you wish to animate 
# 3) Update them in each frame 

# Create a random number generator. 
rng = np.random.default_rng() 
rand = rng.random 

# Define number of steps for each random walk 
num_steps = 100 

'''Define an empty figure of the desired size '''
# Clear anything left over from prior runs 
plt.close('all') 
bound = 20 

# Define a figure object for the movie
fig = plt.figure()

# Define boundaries for the figure object
ax = plt.axes(xlim=(-bound, bound), ylim=(-bound, bound)) 

'''Define an empty line and point objects with no data'''
# Note: The empty lines and point objects will be updated during each frame of the animation 
# Define a line to show path 
my_line, = ax.plot([], [], lw=2) 

# Define a dot to show the current position
my_point, = ax.plot([], [], 'ro', ms=9)

'''Generate Random Walk Data'''
# Generate random steps: +/- 1
x_steps = 2*(rand(num_steps) < 0.5) - 1 
y_steps = 2*(rand(num_steps) < 0.5) - 1 

# Sum the steps to obtain the position of the walker
x_coordinate = x_steps.cumsum() 
y_coordinate = y_steps.cumsum() 

'''Create Animation'''
# Define a function to generate each frame of the animation, which updates the line and position of the walk
def get_step(n, x, y, this_line, this_point): 
    this_line.set_data(x[:n+1], y[:n+1])
    this_point.set_data([x[n]], [y[n]])
    return this_line, this_point 

# Call the animator and create the movie 
my_movie = FuncAnimation(fig, get_step, frames=num_steps, fargs=(x_coordinate, y_coordinate, my_line, my_point) )  

# Save the movie in the current directory 
my_movie.save('random_walk.mp4', fps=30, dpi=300, writer = 'ffmpeg')