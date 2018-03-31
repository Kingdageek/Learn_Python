#pi.py

# Mathematician Srinivasa Ramanujan's formula for computing a numerical
# approximation of PI

def estimate_pi():
	from math import sqrt, factorial
	total = 0
	k = 0
	while True:
		temp = ((factorial(4 * k) * (1103 + 26390 * k)) /
			((factorial(k)) ** 4 * (396 ** (4*k))))
		total += temp
		if temp < 1e-15:
			break
		k += 1
	PI = ((2 * sqrt(2)/ 9801) * total) ** -1
	return PI

print("Approximate value for pi is", estimate_pi())
input()
