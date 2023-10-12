import numpy as np

A = np.random.randn(100,100)
A = (A+np.transpose(A))/2 # Symmetrize
S, U = np.linalg.eig(A)
s = np.diag(A)

