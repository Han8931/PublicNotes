import numpy as np

Theta_hat = 0.29
theta = 0.25
N = 1000
sigma = np.sqrt(theta*(1-theta))
Z_hat = (Theta_hat-theta)/(sigma/np.sqrt(N))
print(Z_hat)
