import numpy as np

''' --- Importing Data with File --- '''
''' Method 1 '''
# Definition: Load the dataset and turn it into an array
# Note: A path can be used to import data as well

# Import Data using Method 1
data_set = np.loadtxt("HIVseries.csv", delimiter=',') # Use delimiter ',' for .csv files

# Print Imported Array
print(data_set) 

''' Method 2 '''
# Definition: Use an Object to read the file and store its content

# Create an object that can read the file 
my_file = open("HIVseries.csv") 

# Define a temporary place to store data
temp_data = [] 

# Loop over each line in the file
for line in my_file: 
    print(line)

    # Separate values based on comma location
    x, y = line.split(',') 

    # Stores values as an ordered pair of x and y
    temp_data += [ (float(x), float(y)) ] 
    
my_file.close()

# Convert temp_data to an array
data_set = np.array(temp_data) 


''' --- Importing Data from Web --- '''
# Import Object to Import Data from Web
from urllib.request import urlopen 

# Open URL and convert its content into an array using np.loadtxt
web_file = urlopen( "https://www.physics.upenn.edu/biophys/" + 
                   "PMLS/Datasets/01HIVseries/HIVseries.csv") 
data_set = np.loadtxt(web_file, delimiter=',') 

