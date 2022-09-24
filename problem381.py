#Project Euler Problem 381 - (prime-k) factorial

import math,time

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

#(p-1)! = -1modp (Wilson's theorem)=>
#(p-1)(p-2)! = -1modp => 
#(p-2)! = -1*inv(p-1)modp = 1modp
#(p-2)! = (p-2)(p-3)! = 1modp =>
#(p-3)! = inv(p-2)*1modp = (p-2)/2 modp

#(p-3)! = (p-3)(p-4)!modp => (p-4)! = inv(p-2)*inv(p-3)modp 
#                                   = inv(p-3)modp

#(p-5)! = inv(p-2)*inv(p-3)*inv(p-4)modp 

def S(p):
    tot = 0
    #modular inverse using extended Euclidean Algorithm
    for k in range(1,5+1):
        if k==1:
            tot+=-1
        elif k==2:
            tot+=1
        elif k==3:
            tot+=modinv(p-2,p)
        elif k==4:
            tot+=modinv(p-3,p)*modinv(p-2,p)
        elif k==5:
            tot+=modinv(p-2,p)*modinv(p-3,p)*modinv(p-4,p)
    return tot % p

#sieve for prime generation up to 100
def sieve(n):
    sieve_list = [True]*n 
    for i in range(2, int(n**0.5 + 1)):
        if sieve_list[i] == True:
            for j in range(i*i, n, i): 
                sieve_list[j] = False
   
    primes = []
    for i in range(2, n):
        if sieve_list[i] ==True: 
            primes.append(i)
    return primes

#sample inputs: m=5,M=100 (sup)
#sample outputs: sum (S(p)) = 480

primes = sieve(10**8)
#remove the first two primes, 2,3
primes = primes[2:]

t0 = time.time()
print(sum(S(p) for p in primes))
t1 = time.time()
print("--Elapsed time:-- %s seconds" % int(t1-t0))
