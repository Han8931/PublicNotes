import scipy.stats as stats
import numpy as np

# Normal Distribution
alpha = 0.05
mu = 0
sigma = 1
z = stats.norm.ppf(1-alpha/2, mu, sigma) # inverse of the CDF. 
print(z)


# Studnet-t Distribution
alpha = 0.05
nu = 13 # degree of freedom
z = stats.t.ppf(1-alpha/2, nu) # inverse of the CDF. 
print(z)
