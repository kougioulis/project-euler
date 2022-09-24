import math

def p(m):
    prod=1
    for i in range(1,m+1):
        prod = prod*((2*i/(m+1))**i)
    return math.floor(prod)

#sample input: m=10
#sample output: p(m) = 4112 
s=0
for m in range(2,15+1):
    s += p(m)

print(s)
