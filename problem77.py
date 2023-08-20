#Project Euler Problem 77 - Prime Summations 

import time

tic = time.time()

def sieve(n):
    prime_list = [True] * (n+1)
    prime_list[0] = prime_list[1] = False
    for i in range(2, int(n**0.5)+1):
        if prime_list[i]:
            for j in range(i*i, n+1, i):
                prime_list[j] = False
    return prime_list

#use dynamic programming similarly to Problem 31
def summations(n):
    ways = [1] + [0] * n
    prime_list = sieve(n)
    primes = [p for p in range(2, n+1) if prime_list[p]]
    for p in primes:
        for i in range(p, n+1):
            ways[i] += ways[i-p]
    return ways

upper_bound = 80
ways = summations(upper_bound)
index = 0

while ways[index] <= 5000:
    index += 1
print(index)

tac = time.time()

print("Elapsed time: %.2f seconds" % (tac-tic))