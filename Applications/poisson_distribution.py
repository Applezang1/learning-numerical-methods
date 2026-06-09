import numpy as np, matplotlib.pyplot as plt, scipy.special as sc

'''--- Poisson Distribution---'''
# Definition: Discrete probability distribution of an event with a specific probability after a fixed number of trials

'''Create Random Distribution Object'''
rng = np.random.default_rng()
random = rng.random
ax = plt.gca()

# Define number of coin flip
N = 1000 

# Define number of times you expect heads to show up
M = np.arange(0, N) 

'''Calculate the Probability of landing heads M times (heads: 8%)'''
# Poisson PMF: P(k) = (e^(-λ) * λ^k) / k!, Heads = 8% chance
# Poisson PMF: Probability of the coin coming up heads M times in 1000 flips
poisson = (np.e**-80 * 80**M)/sc.factorial(M, exact = False)

'''Simulating N coin flips trials'''  
T = 100 # Number of coin flip trials
total_heads = []

# Count Number of Total heads from T coin flip trials and store it as a list
for i in range(T):
    num_heads = random(N) > 0.92 
    num_heads = np.sum(num_heads)
    total_heads.append(num_heads)

# Convert to a NumPy Array
total_heads = np.array(total_heads)

'''Plotting the Graph''' 
plt.hist(total_heads, bins=np.arange(-0.5, N + 1.5, 1), edgecolor='black')
plt.plot(M, poisson*T)
ax.set_xlabel("Number of Heads per Trial")
ax.set_ylabel("Frequency (Percentage of Achieving)")
plt.show()


