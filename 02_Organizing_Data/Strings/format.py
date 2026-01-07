import numpy as np

''' --- Method 1: format() --- '''
# {} brackets represents a placeholder for .format()  

# Example 1: {:.5f} means pi to 5 decimal places as a float
print("The value of {} is approximately {:.5f}".format('pi', np.pi))

# Example 2: {n:d} means (n+1)th argument as a decimal (base 10) integer
s = "{1:d} plus {0:d} is {2:d}" 
print(s.format(2, 4, 2+4))

# Example 3: {2} or {3} represents the element in format, not all arguments need to be used 
print("Every {2} has its {3}.".format('dog', 'day', 'rose', 'thorn'))

# Example 4: {0[2]} means 3rd element of first argument and g means general format (express in fewest characters possible)
print("The third element of the list is {0[2]:g}.".format(np.arange(10))) 

''' --- Method 2: $ (Modulo) Formatting --- '''
# Note: For %, all arguments have to be used and they are based on the order its listed out
# %s: insert string, %d = inset decimal (base 10) integer, ...

# Example 1: %s 
print("The value of %s is approximately %.5f" % ('pi', np.pi,))

# Example 2: %d
s = "%d plus %d is %d" 
print(s % (2, 4, 2+4))

