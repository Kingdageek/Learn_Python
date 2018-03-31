import re
import numpy as np 
import matplotlib.pyplot as plt 

# from moore.csv, we need only the transistor counts
# and the years. We're using 're' cos the data contains
# commas and wikipedia references in []
# our regex should match any non-decimal digit and replace
# it with an empty string.
# Our plot would be Log(Tc) AGAINST time (in years)

X = []
Y = []

# compile our regex into an object. Makes it more efficient

non_decimal = re.compile(r"[\D]+")

with open("moore.csv") as file:
	for line in file:
		record = line.split("\t")
		# do regex search and replace functionality with sub() then cast to int
		x = int(non_decimal.sub("", record[2].split("[")[0])) # year is in the 3rd column
		y = int(non_decimal.sub("", record[1].split("[")[0])) # tc is in the 2nd column
		X.append(x)
		Y.append(y)

# convert X,Y to numpy arrays, easier to work with

X = np.array(X)
Y = np.array(Y)

# let's see the raw data in its exponential form
plt.scatter(X,Y)
plt.show()

# for the linear equation plot
Y = np.log(Y)
# plt.scatter(X, Y)
# plt.show()

# To find our line of best fit
# Yhat = aX + b

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

print("a:", a, "b:", b)
# calculate the predicted Y - Yhat (line of best fit)
Yhat = a * X + b

# plot everything
plt.scatter(X, Y)
plt.plot(X, Yhat)
plt.show()

# to find the R squared to know how efficient our model is
d1 = Y - Yhat
d2 = Y - Y.mean()
ss_res = d1.dot(d1)
ss_tot = d2.dot(d2)
r_2rd = 1 - (ss_res/ss_tot)

print("R squared is:", r_2rd)

# To calculate the time it would take to double
# log(tc) = a * year + b
# tc = exp(a * year) * exp(b) --------------- (*)
# 2tc = 2 * exp(a * year) * exp(b)
# 2tc = exp(ln(2)) * exp(a * year) * exp(b)
# 2tc = exp(a * year + ln(2)) * exp(b)
# Transistor doubles after some time. Let's say It's become
# double in year 'year2' then from (*):
# exp(b) * exp (a * year2) = exp(a * year1 + ln(2)) * exp(b)
# After simplification: 
# year2 = year1 + ln(2)/a
# which basically means it takes ln(2)/a years for tc to double

time_to_double = np.log(2)/a
print("It takes",time_to_double,"years for transistor count to double")