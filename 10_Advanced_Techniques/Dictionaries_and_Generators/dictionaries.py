import numpy as np
'''--- Dictionaries ---''' 
'''Method 1 (Storing Values in Dictionaries)'''
# N is the number of steps, L is the desired x-value location of a person, and p is the probability of moving to the right
parametersA = {'N': 1000, 'L': 10, 'p': 0.5}
parametersB = dict(N = 1000, L = 100, p = 0.5)

'''Method 2 (Storing Values in Dictionaries)'''
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

# Store the parameters with the 'input' key and the results of first_passage with the 'results' key
data = {} 
data['A'] = {'input': parametersA, 
             'results': first_passage(parametersA['N'],
                                      parametersA['L'],
                                      parametersA['p'])} 
data['B'] = {'input': parametersB, 
             'results': first_passage(parametersB['N'],
                                      parametersB['L'],
                                      parametersB['p'])}
print(data)

# Dictionary Function: Call dictionary values with a key, returns value associated to key
print(parametersA['N'])
print(parametersA['p'])

# Dictionary Property: Values are also mutable (able to be changed)
parametersA['L'] = 20 


'''--- Iterate Values in Dictionary ---'''
# Iterate: Go through each item in a collection one at a time 
# Method 1: Iterate over keys 
for k in parametersA.keys():
    print("{} = {}".format(k, parametersA[k]))

# Method 2: Iterate over values 
for v in parametersA.values(): 
    print("{} squared is {}".format(v, v**2))

# Method 3: Iterate over key-value pairs 
for k, v in parametersA.items(): 
    print("The value of {} is {}.".format(k, v)) 




