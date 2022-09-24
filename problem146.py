from sympy import *

num = 2*10**6
candidates=[]

for n in range(1,num+1):
    if isprime(n**2 +1):
        if isprime(n**2 +3):
            if isprime(n**2 +7):
                if isprime(n**2 +9):
                    if isprime(n**2 + 13):
                        if isprime(n**2 + 27):
                            candidates.append(n)


print(sum(candidates))
