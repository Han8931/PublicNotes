import numpy as np
import matplotlib.pyplot as plt

N = 20
x = np.linspace(-1,1,N)
a = np.array([0.5, -2, -3, 4, 6])
y = a[0]+a[1]*x+a[2]*x**2+a[3]*x**3+a[4]*x**4+0.25*np.random.randn(N)

d = 20
X = np.zeros((N,d))
for p in range(d):
    X[:,p] = x**p

lambd = 0.1
A = np.vstack((X, np.sqrt(lambd)*np.eye(d)))
b = np.hstack((y, np.zeros(d)))
theta = np.linalg.lstsq(A,b,rcond=None)[0]

t = np.linspace(-1,1,500)
Xhat = np.zeros((500,d))

for p in range(d):
    Xhat[:,p] = t**p

yhat = np.dot(Xhat, theta)

plt.plot(x,y,'o', markersize=12)
plt.plot(t, yhat, linewidth=4)
plt.show()
