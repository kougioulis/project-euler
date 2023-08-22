#Project Euler Problem 73 - Counting fractions in a range
import math

#input condition: d \leq D

def reduced_proper_fractions(D):
    total = 0 
    for n in range(1,D+1):
        for d in range(D,n,-1):
            if math.gcd(n,d) ==1 and (n/d > 1/3 and n/d < 1/2):
                total+=1
    return total

#sample input: M=8
#sample output: reduced_proper_fractions(8)=3

print(reduced_proper_fractions(12*10**3))
