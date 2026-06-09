# Learning Numerical Methods and Physical Modeling in Python

This repository contains a collection of the implementations of numerical methods and physical modeling concepts present in 'A Student's Guide to Python for Physical Modeling' by Jesse M. Kinder and Philip Nelson. 

## Curriculum 
**[02: Organizing Data](./02_Organizing_Data)**
- [Lists, Tuples, and Arrays](./02_Organizing_Data/Lists_Tuples_Arrays) - Explores array functions such as accessing array elements and slicing an array
- [Strings](./02_Organizing_Data/Strings) - Discusses string formatting techniques and the syntax for raw strings
**[03: Structure and Control](./03_Structure_and_Control)**  
- [Array Operations](./03_Structure_and_Control/Array_Operations) - Explores array operations such as array vectorization and reduction
- [Array_Branching.py](./03_Structure_and_Control/array_branching.py) - Uses arrays for code involving functions
- [Loops.py](./03_Structure_and_Control/loops.py) - Discusses for-loops and while-loops and their applications
- [Nesting.py](./03_Structure_and_Control/nesting.py) - Application of embedding a loop inside another loop
**[04: Data In, Results Out](./04_Data_In_Results_Out)** 
- [Visualizing Data](./04_Data_In_Results_Out/Visualizing_Data) - Explores plotting and parameters for plot customization 
- [Exporting Data](./04_Data_In_Results_Out/Exporting_Data) - Discusses functions for loading, saving, and manipulating data files
- [Importing_Data.py](./04_Data_In_Results_Out/import_data.py) - Discusses methods of importing data from data files or from the web
**[06: Random Number Generation and Numerical Methods](./06_Random_Number_Generation_and_Numerical_Methods)** 
- [Functions.py](./06_Random_Number_Generation_and_Numerical_Methods/functions.py) - Demonstrates examples of function applications for problem-solving
- [Integration.py](./06_Random_Number_Generation_and_Numerical_Methods/integration.py) - Discusses integration techniques, their format, and their application to solving integrals numerically
- [Linear_Algebra.py](./06_Random_Number_Generation_and_Numerical_Methods/linear_algebra_scipy.py) - Explores different linear algebra functions in SciPy, a Python library
- [Ordinary_Differential_Equation_Solver.py](./06_Random_Number_Generation_and_Numerical_Methods/ode_solver.py) - Demonstrates different numerical methods (odeint, solve_ivp) and examples of the application of both numerical methods
- [Root_Finding_Methods.py](./06_Random_Number_Generation_and_Numerical_Methods/root_finding_methods.py) - Explores root finding methods (np.roots, fsolve) and their application to different polynomials
**[08: Images and Animation](./08_Images_and_Animation)**
- [Animation](./08_Images_and_Animation/Animation) - Contains different examples of animation, each animated using techniques such as html_movie and FuncAnimation
- [Image Processing](./08_Images_and_Animation/Image_Processing) - Demonstrates different image manipulation techniques, such as Boolean masking
- [Array_Visualization.py](./08_Images_and_Animation/array_visualization.py) - Explores how to convert an array into an image for visualization purposes
**[10: Advanced Techniques](./10_Advanced_Techniques)**
- [Dictionaries and Generators](./10_Advanced_Techniques/Dictionaries_and_Generators) - Explores the syntax for dictionaries and introduces generators for memory-efficient data processing. Also demonstrates other advanced techniques such as list comprehension and enumeration
- [Tools for Data Science](./10_Advanced_Techniques/Tools_for_Data_Science) - Demonstrates Pandas as a data storage library and compares its DataFrame structure to NumPy arrays
**[Applications](./Applications)**
- [Brownian Motion](./Applications/brownian_motion.py) - Defines a function that computes the random movement of a particle over discrete time steps and plots its trajectory and frequency of final displacement values
- [Beta Gal Activity Model A](./Applications/g149novick_dat_modelA.py) - Computes beta gal activity over time steps using a model and compares the model data to the experimental data A through a plot
- [Beta Gal Activity Model B](./Applications/g149novick_dat_modelB.py) - Computes beta gal activity over time steps using a model and compares the model data to the experimental data B through a plot
- [Beta Gal Activity Exponential Model](./Applications/g149novick_exp_model.py) - Plots the output of the model beta gal activity over time steps given different sets of parameters 
- [HIV Model](./Applications/hiv_model.py) - Defines a function that computes the viral load of HIV over time periods and compares the model data to the experimental data of HIV viral load through a plot
- [Monte Carlo Random Walk](./Applications/monte_carlo_random_walk.py) - Uses the Monte Carlo Process to track the trajectory of a person's random walk
- [Poisson Distribution](./Applications/poisson_distribution.py) - Computes the likelihood of a probabilistic event happening a set number of times throughout a fixed time interval
- [Poisson Process](./Applications/poisson_process.py) - Tracks the time interval between neighboring probabilistic events and plots its frequency in a histogram
