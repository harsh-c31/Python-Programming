import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
#generating random dataset for linear regression
np.random.seed(42)
X=np.random.rand(50,1)*100
Y=3.5*X+np.random.randn(50,1)*20
#creating and training the data model for linear regression
model=LinearRegression()
model.fit(X,Y)
#predicting the values
Y_predict=model.predict(X)
plt.figure(figsize=(8,6))
plt.scatter(X,Y,color='blue',label='Data')
plt.plot(X,Y_predict,color='red',linewidth=2,label='Regression Line')
plt.title('Linear Regression On Random Dataset')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()