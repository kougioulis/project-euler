import math
import sympy


def sieve(n):
    sieve_list = [True]*n #boolean list of length n to keep track of the sieve
    for i in range(2, int(n**0.5 + 1)):
        if sieve_list[i] == True:
            for j in range(i*i, n, i): #start crossing out from the sieve
                sieve_list[j] = False

    final = []
    for i in range(2, n):
        if sieve_list[i] ==True: #if not crossed out then prime
            final.append(i)
    return final

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
