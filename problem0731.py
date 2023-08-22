import math

n = 100
s = 0

#look for k such that 3^k > n => k = log_3 k 

for k in range(1,int(math.log(n,3)+1)):

    num = pow(10,n-3**k-1,3**k) #compute mod3^k for calculation
    num %= 3**k

    s += num/3**k
s -= int(s) #keep fractional part at each iteration

#get first 10 digits of fractional part
print(int(s*10**10))
