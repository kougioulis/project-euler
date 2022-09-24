import math 
import sympy

#def is_prime(n):
#    for i in range(2,int(math.sqrt(n))+1):
#        if (n%i) == 0:
#            return False
#    return True

def mobius(n):
    if n == 1:
        return 1

    # For a prime factor i check if i^2 is also a factor.
    p = 0
    for i in range(1, n+1):
        if (n%i == 0 and sympy.isprime(i)):
            # Check if N is divisible by i^2
            if (n % (i*i) == 0):
                return 0
            else:
                #i occurs only once, increase f
                p += 1

    # All prime factors are contained only once
    # Return 1 if p is even otherwise -1
    if(p % 2 != 0):
        return -1
    else:
        return 1

def q(n):
    return int(6*n/math.pi**2) + int(math.sqrt(n))


squarefree_total = 0
n = 2**20

for i in range(1,n):
    if (mobius(i) != 0):
        squarefree_total +=1

print(squarefree_total)
print(q(n))
