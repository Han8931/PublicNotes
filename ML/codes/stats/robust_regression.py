import pdb
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_legendre
from scipy.optimize import linprog

# Least absolute deviation regression or robust regression
# Linear programming with simplex method


N = 50
x = np.linspace(-1,1,N)
