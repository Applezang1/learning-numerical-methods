import numpy as np, matplotlib.pyplot as plt, scipy.special as sc

'''--- Poisson Process ---'''
# Definition: an ordered collection of random events in a set number of continuous time intervals

'''Create Random Distribution Object'''
rng = np.random.default_rng()
random = rng.random

# Define the number of coin flip
N = 1000000 

# Define the number of times you expect heads to show up
M = np.arange(0, N, 1)

'''Count Number of Total heads from N coin flips'''
num_heads = random(N) > 0.92 

# Returns the indices where the value of the array isn't a zero 
head_frequency = np.nonzero(num_heads) 

# Compute the time intervals between the indices of heads
head_frequency = np.diff(head_frequency)

# Flatten the array of time intervals
head_frequency = head_frequency.flatten()

# Compute the average sum of the time intervals between adjacent heads
average_sum = np.mean(head_frequency)
print(f"The average waiting time in between adjacent heads was {average_sum.round(3)} flips")

'''Plotting the Graph''' 
ax = plt.gca()
plt.hist(head_frequency, bins = np.arange(-0.5, 50, 1), edgecolor = 'black')
ax.set_xlabel("Waiting Times in Between Heads")
ax.set_ylabel("Frequency")
plt.show()



