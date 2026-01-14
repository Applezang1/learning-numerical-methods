import numpy as np

''' --- Branching --- '''
# Definition: Use of functions to make decisions
# Note: Never compare floats with == or !=, use integers or inequalities

'''Example of Branching'''
# Define Max Number of Trials
maxTrials = 5 

# Determine the square root of inputted number for max number of trials
for trial in range(1, maxTrials+1): 
    userInput = input('Pick a number: ')
    number = float(userInput)
    if number < 0: # Example of branching: if number is less than 0 then reject it
        print('The square root is not real.')
    else: 
        print('The square root of {} is {:.4f}. '.format(number, np.sqrt(number)))
    userAgain = input('Try another [y/n]? ')  
    if userAgain != 'y': 
        break 

# Check to determine if the loop exited normally 
if trial >= maxTrials: 
    print('Sorry, only {} per customer.'.format(maxTrials))
elif userAgain == 'n': 
    print('Bye!')
else: 
    print('Sorry, I did not understand that.') 


''' --- np.all --- '''
# Function: Returns True only if all the elements in the array is True 
# Define a 1D Array
x = np.arange(1, 10)

# Use np.all to validate whether the array is positive
if np.all(x>0): 
    print("This array is safe for logarithms.")
else: 
    print("This array is dangerous for logarithms")


''' --- np.any --- '''
# Function: Returns True only if at least one of the elements in the array is True 
# Define a 1D Array
x = np.arange(1, 10)

# Use np.any to check whether a negative term exists in the array
if np.any(x<=0): 
    print("This array is dangerous for logarithms.")
else: 
    print("This array is safe for logarithms")

