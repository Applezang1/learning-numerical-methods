import numpy as np

''' --- np.hstack --- '''
# Note: Both arrays MUST have the same dimensions
x = np.zeros( (2, 3) )
y = np.ones((2, 3))

# H_stack Output: Combined array with the original # of rows (2 in this case)
h = np.hstack( [x, y] )
print(f'Output of H_stack: \n {h}\n')


''' --- np.vstack --- '''
# Note: Both arrays MUST have the same dimensions
x = np.zeros( (2, 3) )
y = np.ones((2, 3))

# V_stack Output: Combined array with the original # of columns (3 in this case)
i = np.vstack( [x, y] )
print(f'Output of V_stack: \n {i}\n')
