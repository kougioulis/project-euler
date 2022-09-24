import math

n = 10**8

m = int(math.log(n,3))
tot = 0
for k in range(1,m+1):
    den = 3**k
    exp = n - den - 1
    num = pow(10,n-3**k -1,3**k)
    tot += num/(3**k) 
tot -= int(tot)
print(int(tot*10**10))
