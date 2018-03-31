# prime_sieve.py
# sieve of erathosthenes
import math
import pprint
def prime_sieve(size):
    #sieve = [False, False] + [True] * (size-2)
    sieve = [True] * size
    sieve[0], sieve[1] = False, False
    #sieve[1] = False
    for i in range(2, int(math.sqrt(size) + 1)):
        pointer = i * 2 # multiples of i
        while pointer < size:
            sieve[pointer] = False
            pointer += i # continue multiples
    primes = []
    for i in range(size):
        if sieve[i] == True:
            primes.append(i)
    return primes

pprint.pprint(prime_sieve(1000))
