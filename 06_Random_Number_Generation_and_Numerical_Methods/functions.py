import numpy as np

'''--- Examples of Functions ---'''
'''Example 1'''
# Define a Function to Compute Taxicab Metric Distance
def taxicab(pointA, pointB): 
    ''' 
    Taxicab metric for computing distance between points A and B. 
        pointA = (x1, y1)
        pointB = (x2, y2)
    Returns |x2-x1| + |y2-y1|. Distances are measured in city blocks
    '''
    interval = abs(pointB[0] - pointA[0]) + abs(pointB[1] - pointA[1])
    return interval 

# Define Parameters 
fare_rate = 0.4 
start = (1,2)
stop = (4,5)

# Compute the trip cost based on parameters
trip_cost = taxicab(start, stop) * fare_rate 
print(f'Trip Cost: {trip_cost}') 

# Define a Function to Compute Travel Distance
def travel_distance(pointA, pointB): 
    distance = np.sqrt((pointB[1] - pointA[1])**2 + (pointB[0] - pointA[0])**2)
    return distance 

# Compute the Travel Distance
print(f"The distance is {travel_distance(start, stop)}.") 

'''Example 2'''
# Define a Function to Compute Distance based on Metric
def distance(pointA, pointB=(0,0), metric='taxi'): 
    """
    Return distance in city blocks between points A and B 
    If metric is 'taxi', (or omitted), use taxicab metric
    Otherwise, use Euclidean distance 
        pointA = (x1, y1)
        pointB = (x2, y2) 
    If pointB is omitted, use the origin. 
    """ 
    if metric == 'taxi': 
        interval = abs(pointB[0] - pointA[0]) + abs(pointB[1] - pointA[1])
    else: 
        interval = np.sqrt( (pointB[0] - pointA[0])**2 \
                           + (pointB[1] - pointA[1])**2 )
    return interval

# Compute distance given point locations
print(distance( (3,4), (1,2), 'euclid')) 

'''Example 3'''
# Define a function that rotates a two-dimensional vector given the vector and rotation angle
def rotate_vector(vector, angle): 
    """
    Rotate a two-dimensional vector through given angle.
        vector = (x, y)
        angle = rotation angle in radians (counterclockwise)
    Returns the image of a vector under rotation as a NumPy array
    """
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    return np.dot(rotation_matrix, vector)

# Define Parameters
vec = [1, 1]
theta = np.pi/2 

# Compute Vector Rotation given Parameters
r = rotate_vector(vec, theta)
print(f"The value of r is {r}") 
x, y = rotate_vector(vec, theta)
print(f"The value of x is {x} and the value of y is {y}.") 

'''Example 4'''
# Define a function that returns the cumulative average of an array
def running_average(x): 
    # Define an array structure to store results
    y = np.zeros(len(x))
    # Define a current running sum of elements of x
    current_sum = 0.0 
    for i in range(len(x)): 
        current_sum += x[i] # Increment sum
        y[i] = current_sum / (i+1) # Update running average
    return y