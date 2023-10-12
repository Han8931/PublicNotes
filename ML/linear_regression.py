import pdb
import numpy as np
from sklearn.linear_model import LinearRegression

X = [[6], [8], [10], [14], [18]]
y = [[7], [9], [13], [17.5], [18]]

model = LinearRegression()
model.fit(X,y)
print(model.predict([[12]]))
print(f"Model scores: {model.score()}") 

polyFeature = PolynomialFeatures(degree=2)

train = polyFeature.fit_transform(X_train)
test = polyFeature.fit_transform(X_test)

regressor = LinearRegression()
regressor(train, y_train)
test = regressor.transform(xx.reshape())


X_cross = np.matmul(np.linalg.pinv(np.matmul(X, X.T)), X)


