#Project Euler Problem 47 - Distinct prime factors

import time

tic = time.time()

#modified sieve for counting prime factors
def sieve_for_prime_factors(n):
    sieve_list = [0] * (n + 1) #number of prime factors
    for i in range(2, n + 1):
        if sieve_list[i] == 0:
            for j in range(i, n + 1, i):
                sieve_list[j] += 1
    return sieve_list

consecutive = 4
sieve_list = sieve_for_prime_factors(10**6)

for i in range(2, 10**6):
    if sieve_list[i] == consecutive:
        if sieve_list[i + 1] == consecutive:
            if sieve_list[i + 2] == consecutive:
                if sieve_list[i + 3] == consecutive:
                    print(i)
                    break

tac = time.time()

print("Elapsed time: %.2f seconds" % (tac - tic))