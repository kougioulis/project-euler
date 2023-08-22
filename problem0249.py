#Project Euler Problem 249 - Prime Subset Sums

import time 
import numpy

tic = time.time()

def sieve(n):
    sieve_list = [True]*(n+1)
    sieve_list[0] = sieve_list[1] = False
    for i in range(2, int(n**0.5)+1):
        if sieve_list[i]:
            for j in range(i**2, n+1, i):
                sieve_list[j] = False
    return sieve_list

def prime_subset_sums(n):
    primes = sieve(n)
    count = [0]*(n+1)
    count[0] = 1
    for p in range(2,n+1):
        if primes[p]:
            for i in range(n, p - 1, -1):
                count[i] = (count[i] + count[i-p]) % 10**16  #truncate to last 16 digits to avoid overflow

    #consider prime counts only
    prime_counts = [count[i] for i in range(len(count)) if primes[i]]
    return sum(prime_counts) % 10**16

print("The number of prime subset sums is:", prime_subset_sums(5000))

tac = time.time()

print("Elapsed time: %.2f seconds" % (tac-tic))

