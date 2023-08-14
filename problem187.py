#Project Euler Problem 187 - Semiprimes

import time
import math

tic = time.time()

def sieve(n):
    sieve_list = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if sieve_list[i]:
            for j in range(i * i, n + 1, i):
                sieve_list[j] = False
    return sieve_list

def prime_list(n):
    sieve_list = sieve(n)
    prime_list = [i for i, is_prime in enumerate(sieve_list) if is_prime and i >= 2]
    return prime_list

def p(n): # prime counting function, \pi(n) = \left\{ number of primes less than or equal to n \right\} (assuming n < 10^8)
    return len(prime_list(n))

 #semiprime counting function, \pi_2(n) = \left\{ number of semiprimes less than or equal to n \right\} (assuming n < 10^8)
 #see https://mathworld.wolfram.com/Semiprime.html and https://sci.math.research.narkive.com/6VgsgJBj/the-number-of-semiprimes
def p2(n):
    primes = prime_list(n)
    count = 0
    for k in range(1, len(primes)+1):
        if primes[k-1]*primes[k-1] > n: 
            break
        val = p(n // primes[k-1]) - k + 1
        count += val

    return count

N = 10**8
result = p2(N)

print(result)

tac = time.time()

print("Elapsed time: %.2f seconds" % (tac - tic))