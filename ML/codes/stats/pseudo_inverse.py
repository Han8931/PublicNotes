import numpy as np

# x'*y
x = np.array([1,0,-1])
y = np.array([3,2,0])
z = np.dot(x,y)
print(z)

# Norm
x = np.array([1,0,-1])
x_norm = np.linalg.norm(x)
print(x_norm)

# Weighted Norm x'*w*y
W = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x = np.array([[2],[-1],[1]])
z = np.dot(x.T, np.dot(W,x))
print(z)

X      = np.array([[1, 3], [-2, 7], [0, 1]])
XtX    = np.dot(X.T, X)
XtXinv = np.linalg.inv(XtX) #(x'*x)^-1
print(XtXinv)

# PseudoInverse
X      = np.array([[1, 3], [-2, 7], [0, 1]])
y      = np.array([[2],[1],[0]])
beta   = np.linalg.lstsq(X, y, rcond=None)[0] # Least square solution
print(beta)

