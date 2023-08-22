#Project Euler Problem #97 - Large Non-Mersenne Prime

import math 
import time

tic = time.time()

def last_k_digits(n, k):
    return n % 10**k

print("Last 10 digits:", last_k_digits(28433 * pow(2, 7830457) + 1, 10))

tac = time.time()

print("Elapsed time: %.2f seconds" % (tac-tic))
