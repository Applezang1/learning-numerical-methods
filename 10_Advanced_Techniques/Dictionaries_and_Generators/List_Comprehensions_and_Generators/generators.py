import numpy as np 
'''--- Generators ---'''
# Function: Provides values only when requested 
# Application: Generators are more memory efficient than other data types like NumPy arrays and lists

'''Example of Generators (next) '''
# Define a generator expression (marked by parentheses) filled with numbers
G = (n**2 for n in range(100))

# Ask for the first value of the generator expression, where n = 0
print(next(G)) 

# Ask for the first value of the generator expression, where n = 1
print(next(G)) 

'''Comparison of Different Data Types and Sizes'''
# Initialize random data points for storage
N = 10**6 
rng = np.random.default_rng() 

# Method 1: Store in NumPy Array
r_array = rng.random(N) 
print("Size of array: {}".format(r_array.__sizeof__()))

# Method 2: Store in Python List
r_list = [rng.random() for n in range(N)]
print("Size of list: {}".format(r_list.__sizeof__())) 

# Method 3: Store in generator
r_iter = (rng.random() for n in range(N))
print("Size of generator: {}".format(r_iter.__sizeof__()))




