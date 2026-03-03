import numpy as np, matplotlib.pyplot as plt 

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
            print("First passage of x={} occured after {} steps.".format(L, n))
        return n 
    else: 
        if message: 
            print("Did not reach x={} after {} steps.".format(L, N))
        return np.nan

'''--- Double-Starred Expressions ---'''
# Function: Gives ability to pass key/value pairs to a function via dictionary 
# Define parameters in a dictionary
parametersD = dict(N = 1000, L = 25, p = 0.5, message = True)

'''Use of Double-Starred Expression'''
# Define a loop where key/value pairs in the parameter dictionary are passed through the first_passage function
for i in range(20): 
    first_passage(**parametersD)
    print(parametersD)


'''--- Starred Expressions ---''' 
# Function: Allows you to graph multiple lines with ease by storing into a list
# Define an array of time steps
t = np.linspace(-2*np.pi, 2*np.pi, 201) 

# Define a list that stores the domain, function, and format of line 1
line1 = [t, np.sin(t), 'r-'] 

# Define a list that stores the domain, function, and format of line 2
line2 = [t, np.cos(t), 'k--'] 

'''Use of Starred Expression'''
# Graph lines 1 and 2 using starred expression
plt.plot(*line1, *line2) 
plt.show() 

# Define a set of parameters
parametersC = (1000, 25, 0.5, True)

# Use starred expression to put values of parametersC into first_passage
for i in range(20): 
    first_passage(*parametersC)
    print(parametersC)