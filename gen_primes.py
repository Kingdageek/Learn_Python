# gen_primes.py
import pprint
import math
def gen_primes(n):
	primes = [2]
	for i in range(3,n):
		for k in range(2,int(math.sqrt(i)) + 1):
			if i % k == 0: break
		else: primes.append(i)
	return primes

pprint.pprint(gen_primes(1000))
