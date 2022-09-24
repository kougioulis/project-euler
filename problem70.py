import math
import time
from sympy import primefactors

#similar to Problem 69

def sieve(n):
    sieve_list = [True]*(n+1)
    sieve_list[0] = sieve_list[1] = False

    for i in range(int(n**0.5 + 1)):
        if sieve_list[i] == True:
            for j in range(i*i, len(sieve_list), i):
                sieve_list[j] = False

    return sieve_list

M = 10**7
lst = sieve(M)


def phi(n):
    if lst[n]:
        return n-1 #if n is prime then phi(n) = n-1
    else:
        prod = n
        for p in primefactors(n):
            prod *= (1-(1/p))
    return (prod)

def are_permuted(a,b):
    return sorted(list(str(a))) == sorted(list(str(b)))

t0 = time.time()

minimum = 10**9 #a large number as a supremum
n = 10**9

for k in range(2,lim):
    if k/phi(k) < minimum and are_permuted(k,int(phi(k))):
        n = k
        minimum = k/phi(k)

print(n)

t1 = time.time()
print("Elapsed time: %s seconds" % (t1 - t0))
