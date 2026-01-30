import numpy as np, matplotlib.pyplot as plt 
from scipy.integrate import odeint 
from scipy.integrate import solve_ivp 

'''--- Numerical Solution of Differential Equations (odeint) ---'''
# Ordinary Differential Equation: Equality involving the function and its derivative 
# Syntax: y = odeint(F, y0, t)
# F: function F(y, t)
# y0: one-dimensional array with the initial value of y
# t: array of t values at which y is to be computed 
# y: array of the values of y(t) at points specified in t 

# Define a function that returns derivatives for a second-order ODE
def F(y, t): 
    # Define a list structure to store derivatives 
    dy = [0, 0] 
    # Store first derivative of y(t)
    dy[0] = y[1] 
    # Store second derivative of y(t) 
    dy[1] = -y[0] 
    return dy 

'''Example 1: ODE solver for harmonic oscillator'''
# Convert second-order ODE of a simple oscillator into a system of first-order ODE
def F(y, t): 
    # Define a list structure to store derivatives
    dy = [0, 0] 
    # Store first derivative of y(t)
    dy[0] = y[1] 
    # Store second derivative of y(t)
    dy[1] = -y[0]
    return dy  

# Define an array of time values 
t_min = 0; t_max = 10; dt = 0.1 
t = np.arange(t_min, t_max+dt, dt)

# Initialize two sets of initial conditions: 
initial_conditions = [ (1.0, 0.0), (0.0, 1.0) ]

# Compute the y_values of simple oscillator using a numerical integrator
plt.figure()  
for y0 in initial_conditions: 
    y = odeint(F, y0, t)
    # Plot the computed y_values, (Note: y[:,0] gets the y(t) value)
    plt.plot(t, y[:, 0] , linewidth = 2) 

# Compare the Numerical Integrator with the Exact Solution
skip = 5 
t_test = t[::skip] # Compare at a subset of points
plt.plot(t_test, np.cos(t_test), 'bo') # Exact solution for y0 = (1, 0)
plt.plot(t_test, np.sin(t_test), 'ro') # Exact solution for y0 = (0, 1)
plt.show() 

'''Example 2: Harmonic Oscillator for a Spring'''
# Convert second-order ODE of a spring harmonic oscillator into a system of first-order ODE
def F(y, t, spring_constant = 1.0, mass = 1.0): 
    '''Return derivatives for harmonic oscillator: 
        y'' = -(k/m) * y
    y = displacement in [m]
    k = spring_constant in [m] 
    m = mass in [kg] '''
    # Define an array structure to store the derivatives
    dy = [0, 0] 
    dy[0] = y[1]
    dy[1] = -(spring_constant / mass) * y[0]
    return dy  

# Initialize Parameters
y0 = (1.0, 0.0)
t = np.linspace(0, 10, 101)
k = 2.0 
m = 0.5 

# Compute the Numerical Integrator using a dummy function 
def G(y, t): return F(y, t, k, m)
yA = odeint(G, y0, t)

# Compute the Numerical Integrator using key terms
yB = odeint(F, y0, t, args = (k, m)) 


'''--- Numerical Solution of Differential Equations (solve_ivp) ---'''
'''Example 1: Simple Harmonic Oscillator using solve_ivp'''
# Define first order ODE for a simple harmonic oscillator 
def f(t, y): return [ y[1], -y[0] ]

# Define time interval 
t_min = 0 
t_max = 10 

# Initalize initial conditions 
y0 = [1.0, 0.0]
 
# Integrate the ODE using RK45 and plot results 
result = solve_ivp(f, (t_min, t_max), y0)
plt.plot(result.t, result.y[0], '^k', label = 'RK45')

# Initialize array of time series
dt = 0.1 
t_vals = np.arange(t_min, t_max + dt, dt)

# Integrate the ODE using BDF and plot results
result = solve_ivp(f, (t_min, t_max), y0, t_eval = t_vals, method = 'BDF')
plt.plot(result.t, result.y[0], '.r', label = 'BDF')
plt.legend() 
plt.show() 