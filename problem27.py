import math
import sympy

#TODO: use prime sieve list instead of sympy's isprime function (like Problem 69)
max_num = 1
max_prod = 1

def f(a,b):
    tot = 0
    n = 0
    while True:
        if sympy.isprime((n*n) + a*n + b):
            tot +=1
            n +=1
        else:
            break
    return tot

for b in sieve(1000):
    for a in range(1-b,1000):
        if sympy.isprime(1+a+b):
            if f(a,b) > max_num:
                max_num = f(a,b)
                max_prod = a*b 

print(max_prod)
