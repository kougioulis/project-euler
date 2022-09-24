import math
import sympy
import time

#generate a boolean list of the first n natural numbers
#to check whether a number k is prime using a sieve,
#by only accesing the list

def sieve(n):
    sieve_list = [True]*(n+1) 
    sieve_list[0] = sieve_list[1] = False

    for i in range(int(n**0.5 + 1)):
        if sieve_list[i] == True:
            for j in range(i*i, len(sieve_list), i): 
                sieve_list[j] = False

    return sieve_list

#or import sympy and use sympy.divisors
def divisors(n):
    divs = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n/i])
    divs.extend([n])
    return list(set(divs))

t0 = time.time()

M = 10**6
primes = sieve(M)

s=1
lst = sieve(M)

for n in range(1,M):
    #for d in sympy.divisors(n):
    #faster to check every d instead of 
    for d in range(2,int(math.sqrt(n)) +1):
        if not lst[int(d+n/d)]:
            break
        else:
            s+=n

print(s)
t1 = time.time()
print("Elapsed time: %s seconds" % (t1 - t0))
