import math

#d \leq D
D = 10**6

# p/d < a/b => pb < ad => pb < ad -1 => p < (ad-1)/b

#iterate to obtain the smallest fraction 
# r/s < p/d => rd < ps
a=3
b=7
r=0
s=1 #can't divide by zero

for d in range(1,D+1):
    p = math.floor((a*d -1)/b)
    if r*d < p*s:
        r=p
        s=d


#sample input: D = 8
#sample output: 2

print(r)
