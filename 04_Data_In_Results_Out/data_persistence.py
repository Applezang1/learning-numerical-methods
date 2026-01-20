import numpy as np, matplotlib.pyplot as plt, matplotlib

''' --- Loading and Recovering Saved Data --- '''
# Define an array of numbers
x = np.linspace(0, 1, 1001)
y = 3*np.sin(x)**3 - np.sin(x)

# --- np.load --- 
# Property: used for .npy files
x2 = np.load('x_values.npy') 

# --- np.loadtxt --- 
# Property: used for .dat files
y2 = np.loadtxt('y_values.dat') 

# --- np.load (.npz) --- 
# Property: .npz loads multiple arrays
w = np.load('xy_values.npz') 

# Access each element on its own
w['x_vals'] == x 
w['y_vals'] == y  


''' --- Saving Data as Array(s) --- '''
# Define an array of numbers
x = np.linspace(0, 1, 1001)
y = 3*np.sin(x)**3 - np.sin(x)

# --- np.save ---
# Function: Save a single array with extension .npy
np.save('x_values', x) 
np.save('y_values', y)

# --- np.savetxt ---
# Function: Save a single array as a text file, extension of your chocie
np.savetxt('x_values.dat', x) 
np.savetxt('y_values.dat', y)

# --- np.savez ---
# Save multiple arrays with extension .npz 
np.savez('xy_values', x_vals=x, y_vals=y) 


''' --- Saving Figures --- '''
# Obtain current figure object
fig = plt.gcf() 

# Find all compatible file types  
fig.canvas.get_supported_filetypes() 

# Save file with supported file type 
plt.savefig("greatest_figure_ever.pdf") 

# Use matplotlib.rcParams to modify font types in .svg figures
matplotlib.rcParams['svg.fonttype'] = 'none' 


''' --- Writing Readable Data --- '''
# File Name: power.txt

# Open file ('w' indicates that file is opened for writing)
my_file = open('power.txt', 'w')

# Print labels for columns, formatting
print( "N \t\t2**N\t\t3**N" ) 

# Print separator, formatting
print( "---\t\t----\t\t----") 

# Write labels to file, formatting
my_file.write( "N \t\t2**N\t\t3**N\n" ) 

 # Write separator to file, formatting
my_file.write( "---\t\t----\t\t----\n" )

# Loop over integers from 0 to 10 and print/write results 
for N in range(11): 
    print( "{:d}\t\t{:d}\t\t{:d}".format(N, pow(2, N), pow(3, N)) )
    my_file.write( "{:d}\t\t{:d}\t\t{:d}\n". format(N, pow(2, N), pow(3, N))) 
my_file.close()