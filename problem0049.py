#Project Euler Problem 49 - Prime Permutations

import time
from itertools import permutations

tic = time.time()

def sieve(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return primes

#generate up to 1 mil since we are looking for a 4 digit arithmetic sequence of primes
primes = sieve(10**5)

found_seq = False
for num in range(10**4, 10**5): #10**5 -1 is the largest 4 digit integer
    if primes[num] and not found_seq:
        perms = [int("".join(p)) for p in permutations(str(num))]
        perms = sorted(list(set(perms))) #remove dups
        perms = [p for p in perms if primes[p]]
        perms = [p for p in perms if len(str(p)) == 4]
        #select the permutations that are arithmetic sequences of 3330
        for i in range(len(perms)-2):
            if perms[i+2] - perms[i+1] == 3330 and perms[i+1] - perms[i] == 3330:
                print(str(perms[i]) + str(perms[i+1]) + str(perms[i+2]))
                found_seq = True

tac = time.time()

print("Elapsed time: %.2f seconds" % (tac-tic))