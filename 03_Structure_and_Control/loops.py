import numpy as np

''' --- For Loops --- '''
# Example 1: Loop through values of array 'a' and find x using the quadratic formula
# Define Variables
b, c = 2, -1

# Run For Loop over values of 'a'
for a in np.arange(-1, 2, 0.3): 
    x = (-b + np.sqrt(b**2 - 4*a*c)) / (2*a)

    # Print to 4 decimal places
    print("a= {:.4f}, x= {:.4f}".format(a, x)) 

# Example 2: Use Modulo Operator to print the % of the number of a multiple of 100,000
for ii in range(10**6): 
    if ii % 10**5 == 0: 
        print("{:.0f} percent complete". format(100*ii/10**6))

''' --- While Loops --- '''
# Example 1: Decrease value 'a' until the discriminant is positive
# Define Variables
a, b, c = 2, 2, -1

# Run While Loop until solution is achieved
while (b**2 - 4*a*c >= 0): 
    x = (-b + np.sqrt(b**2 - 4*a*c)) / (2*a)
    print("a = {:.4f}, x = {:.4f}". format(a, x))
    a = a - 0.3 
print("Done!") 
