import numpy as np 
import matplotlib.pyplot as plt 


# to load the data

X = []
Y = []

with open("data_1d.csv", "r") as file:
	for line in file:
		x,y = line.split(",")
		X.append(float(x))  	# we want to convert it from string to float
		Y.append(float(y))

# to convert X and Y to numpy arrays they're more useful

X = np.array(X)
Y = np.array(Y)

# let's plot it with matplotlib to see first

plt.scatter(X,Y)
plt.show()

# apply the equations to determine a and b

X2rd_mean = (X ** 2).mean()
mean_X = X.mean()
mean_X_2rd = mean_X ** 2
mean_Y = Y.mean()
mean_XY = (X*Y).mean()

# a and b have a common denominator 
denominator = X2rd_mean - mean_X_2rd

a = (mean_XY - (mean_X * mean_Y)) / denominator
b = ((X2rd_mean * mean_Y) - (mean_X * mean_XY)) / denominator

# calculate the predicted Y - Yhat (line of best fit)
Yhat = a * X + b

# plot everything
plt.scatter(X,Y)
plt.plot(X,Yhat)
plt.show()

# Calculating the r-squared to know how effective our model is
# r_2rd = 1 - (Sum of squares residual/ Sum of squares total)

# ss_res = ((Y - Yhat) ** 2).sum()
# ss_total = ((Y - mean_Y) ** 2).sum()	# numpy's element-wise operations
# r_2rd = 1 - (ss_res/ss_total)

d1 = Y - Yhat
ss_res = d1.dot(d1)
d2 = Y - mean_Y
ss_total = d2.dot(d2)
r_2rd = 1 - (ss_res/ss_total)

print("R squared is: ", str(r_2rd))

scale = "Efficient" if r_2rd > 0.5 else "Inefficient"
print("R squared is", scale)