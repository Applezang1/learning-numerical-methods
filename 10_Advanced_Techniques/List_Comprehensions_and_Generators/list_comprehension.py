import numpy as np 
# Define a function to calculate the number of random steps needed to reach a certain x-value
def first_passage(N, L, p=0.5, message = False): 
    '''
    Return number of steps for first passage of x ==L,
    or give up after N and return np.nan. 
    
    The walker takes steps to the right with probability p
    
    Use message = True to display results.
    ''' 
    rng = np.random.default_rng() # Create a random number generator object 
    dx = 2*(rng.random(N) < p) - 1 # Individual steps 
    x = np.cumsum(dx) # Location after each step 
    at_target = np.nonzero(x==L)[0] 

    if at_target.size > 0: 
        n = at_target[0] + 1
        if message: 
            print("First passage of x={} occurred after {} steps.".format(L, n))
        return n 
    else: 
        if message: 
            print("Did not reach x={} after {} steps.".format(L, N))
        return np.nan
    
'''--- List Comprehensions ---'''
# Definition: a one-line for-loop enclosed in square brackets

'''Example of List Comprehension''' 
# Define an empty dictionary for data storage
data = {} 

# Define an empty dictionary within 'data' to store Simulation A values
data['A'] = {} 

# Define an empty dictionary within 'data' to store Simulation B values
data['B'] = {} 

# Define an empty dictionary within 'data' to store Simulation C values
data['C'] = {} 

# Define and run simulations. 
samples = 500 

# Use list comprehension to put outputs of a for-loop into dictionary values
data['A']['input'] = dict(N=1000, L=10, p=0.5)
data['A']['results'] = [first_passage(**data['A']['input']) for n in range(samples)]

data['B']['input'] = dict(N=1000, L=20, p=0.5) 
data['B']['results'] = [first_passage(**data['B']['input']) for n in range(samples)]

data['C']['input'] = dict(N=1000, L=25, p=0.5)
data['C']['results'] = [first_passage(**data['C']['input']) for n in range(samples)]

# Run more simulations and use "+=" to append new list to old. 
data['A']['results'] += [first_passage(**data['A']['input']) for n in range(samples)]
data['B']['results'] += [first_passage(**data['B']['input']) for n in range(samples)]   
data['C']['results'] += [first_passage(**data['C']['input']) for n in range(samples)] 


