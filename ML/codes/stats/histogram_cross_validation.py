import numpy as np
import matplotlib.pyplot as plt

lambd = 1
n     = 1000
X     = np.random.exponential(1/lambd, size=n)
m     = np.arange(5,200) # Number of bins
J     = np.zeros((195))

for i in range(0,195):
  hist,bins = np.histogram(X,bins=m[i])
  h = n/m[i]
  J[i] = 2/((n-1)*h)-((n+1)/((n-1)*h))*np.sum((hist/n)**2)

plt.plot(m,J);
plt.show()
