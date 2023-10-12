import pdb

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import toeplitz

N = 500
y = np.cumsum(0.2*np.random.randn(N))+0.05*np.random.randn(N) # Generate data

L = 100 # Use previous 100 samples
c = np.hstack((0,y[0:400-1])) # First column
r = np.zeros(L) # First row
X = toeplitz(c,r)
theta = np.linalg.lstsq(X,y[0:400], rcond=None)[0]
yhat = np.dot(X,theta)

plt.plot(y[0:400], 'o')
plt.plot(yhat[0:400], linewidth=4)
plt.show()
