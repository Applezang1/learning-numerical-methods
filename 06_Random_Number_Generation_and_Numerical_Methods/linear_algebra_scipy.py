from scipy.linalg import inv 
import numpy as np

'''--- List of Linear Algebra Functions ---'''
# inv: matrix inverse 
# det: determinant 
# sqrtm: matrix square root 
# expm: matrix exponentation 
# eig: eigenvalues and eigenvectors of a matrix 
# eigh: eigenvalues and eigenvectors of a Hermitian matrix 
# svd: singular value decomposition 

'''Application of LInear Algebra Functions'''
# Define two arrays
a = np.array( [-1, 5] )
C = np.array( [ [1, 3], [3, 4] ]) 

# Compute the dot product between the matrix inverse of C and matrix a
x = np.dot(inv(C), a)
print(f'Compute dot product: {x}')
