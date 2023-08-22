#Project Euler Problem 74 - Digit factorial chains

import time
import math

tic = time.time()

def digit_factorial_sum(n):
    return sum([math.factorial(int(i)) for i in str(n)])

def chain_length(n):
    chain = set()
    chain.add(n)
    next = digit_factorial_sum(n)
    while next not in chain:
        chain.add(next)
        next = digit_factorial_sum(next)
    return len(chain)

count = 0
N = 10**6

for i in range(1,N):
    if chain_length(i) == 60:
        count += 1

print(count)

tac = time.time()

print("Elapsed time: %.2f seconds" % (tac - tic))