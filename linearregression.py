import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# random data
A = [100,110,112,115,117,116,118,120,121,120,117,123]
b = [5.5,5.8,6,5.9,6.2,6.3,6.5,6.6,6.4,6.5,6.7,6.8]

# Visualize data
plt.plot(A,b,'ro')

# Change row vector to column vector
A = np.array([A]).T
b = np.array([b]).T

# Create vector 1cd Do
ones = np.ones((A.shape[0],1), dtype=np.int8)

# Combine 1 and A
A = np.concatenate((A, ones), axis =1)


# Use fomular
x = np.linalg.inv(A.transpose().dot(A)).dot(A.transpose()).dot(b)

# Test data to draw
x0 = np.array([[90,130]]).T
y0 = x0*x[0][0] + x[1][0]

plt.plot(x0,y0)

# Test predicting data
x_test = 12
y_test = x_test*x[0][0] + x[1][0]

print(x[0][0],x[1][0])
#print(y_test)
plt.show()

print(Successfully updated)
