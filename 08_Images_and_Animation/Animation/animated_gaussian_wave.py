'''Generate frames for an animation of moving Gaussian waves'''
import numpy as np, matplotlib.pyplot as plt 
# Import movie, which is a website with a collection of individual images
from html_movie import movie

'''Generate Plotting Data of Gaussian Wave'''
# Define a function for a Gaussian with specified center and spread using array s. 
def gaussian(s, center=0.0, spread=1.0): 
    return np.exp(-2 * (s-center)**2 / spread**2) 

# Define the range of x and y-values for figure
# Note: All lengths are in [m], all times are in [s], and all speeds are in [m/s]. 
x_min, x_max = -4.0, 4.0 
y_min, y_max = -3.0, 3.0 

# Define array of x-values for input 
dx = 0.01 
x = np.arange(x_min, x_max + dx, dx)

# Define the duration and number of frames for the simulation 
tmin, tmax = 0.0, 4.0 
num_frames = 100 
t = np.linspace(tmin, tmax, num_frames)

# Define the initial position and speed of Gaussian waves 
r_speed = 2.0 # Speed of right-moving wave 
r_O = -4.0 # Initial position of right-moving wave 
l_speed = -2.0 # Speed of left-moving wave 
l_O = 4.0 # Initial position of left-moving wave 

'''Create Line Object'''
# Generate a figure and get access to its Axes object
plt.close('all')
fig = plt.figure(figsize=(6, 6))
ax = plt.axes(xlim = (x_min, x_max), ylim = (y_min, y_max))

# Define a line for the right-moving wave 
ax.plot([], [], 'b--', lw=1) 

# Define a line for the left-moving wave
ax.plot([], [], 'r--', lw=1) 

# Define a line for the sum of waves
ax.plot([], [], 'g--', lw=3)

# Store the line objects
lines = ax.get_lines() 

'''Create Movie Animation'''
file_name = "{:03d}_movie.jpg" 

# Define a function to generate frames and save each figure as a separate .jpg file 
for i in range(num_frames): 
    # Update centers of waves 
    r_now = r_O + r_speed * t[i] 
    l_now = l_O + l_speed * t[i] 

    # Get current data for waves 
    yR = gaussian(x, r_now) 
    yL = -gaussian(x, l_now)

    # Update right-moving wave 
    lines[0].set_data(x, yR) 

    # Update left-moving wave 
    lines[1].set_data(x, yL) 

    # Update sum of waves. 
    lines[2].set_data(x, yR + yL) 

    # Save current plot 
    plt.savefig(file_name.format(i)) 

# Use HTML movie encoder to create an HTML document to display the frames as a movie. 
# Note: Open movie.html in web browser to view the movie
movie(input_files='*.jpg', output_file = 'movie.html')