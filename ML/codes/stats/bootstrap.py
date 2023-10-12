import numpy as np
import pdb

X = np.array([72, 69, 75, 58, 67, 70, 60, 71, 59, 65])
N = X.size
K = 1000

Thetahat = np.zeros(K)
for i in range(K):
    idx = np.random.randint(N, size=N)
    Y = X[idx]
    Thetahat[i] = np.median(Y)

M = np.mean(Thetahat)
V = np.var(Thetahat)
print(M, V)
