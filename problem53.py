#Project Euler Problem 53 - Combinatoric Selections

import time
import math

tic = time.time()

def n_choose_r(n,r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r)) #fast way to calculate the binom. coeff.

N = 100

count = 0
for n in range(1,N+1):
    for r in range(1,n):
        if n_choose_r(n,r) > 10**6:
            count += 1

print(count)

tac = time.time()

print("Elapsed Time: %.2f seconds" % (tac-tic))