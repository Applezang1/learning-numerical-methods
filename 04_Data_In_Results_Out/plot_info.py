import matplotlib.pyplot as plt

'''--- Useful Information about Plotting ---'''
# 1. Interactive Plotting: updates graph with every executed plotting command
plt.ion() #Turns interactive plotting on 
plt.ioff() #Turns interactive plotting off 

# 2. Important Notes: 
plt.close() # Closes current figure 
plt.close('all') # Closes all figures
# Note: Supplied arrays for plotting must have the same shape    
# Use 'assert' and 'len' to check for consistent array shape 

# 3. PyPlot uses the objects Axes and Figures to control and manage plots
# Figure: the empty graph, Axes: data and methods needed to draw a graph 
