import math
import time
from sympy import primefactors

#generate a boolean list of the first n natural numbers
#to check whether a number k is prime using a sieve,
#by only accesing the list(O(1) time), instead of searching the 
#list of all primes (O(n) time)

def sieve(n):
    sieve_list = [True]*(n+1)
    sieve_list[0] = sieve_list[1] = False

    for i in range(int(n**0.5 + 1)): #i^2 < n
        if sieve_list[i] == True:
            for j in range(i*i, len(sieve_list), i):
                sieve_list[j] = False

    return sieve_list

M = 10**6
lst = sieve(M)

#compute phi(n) using prime factorization
def phi(n):
    if lst[n]:
        return n-1 #if n is prime then phi(n) = n-1 
    prod = n
    for p in primefactors(n):
        prod *= (1-(1/p))
    return (prod)

#sample input: M=10
#sample output: n=6

maximum= -1 #set infimum as maximum
n = -1

t0 = time.time()

for i in range(2,M +1):
    if i/phi(i) > maximum:
        maximum = i/phi(i)
        n = i

print(n)

t1 = time.time()
print("Elapsed time: %s seconds" % (t1 - t0))
