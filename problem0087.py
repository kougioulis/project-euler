#Project Euler Problem 87 - Prime power triples

import time
import math

tic = time.time()

def sieve(n):
    primes = [True]*(n+1)
    primes[0] = primes[1] = False
    for i in range(2, int(math.sqrt(n))+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return primes

N = 50*10**6
lst = sieve(math.floor(math.sqrt(N))) #search for primes up to sqrt(N)
primes = [i for i in range(len(lst)) if lst[i]]

s = set()

for i in primes:
    for j in primes:
        for k in primes:
            if i**2 + j**3 + k**4 < N:
                s.add(i**2 + j**3 + k**4)
            else:
                break

print(len(s))

tac = time.time()

print("Elapsed time: %.2f seconds" % (tac-tic))