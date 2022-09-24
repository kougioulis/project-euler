#upper bound for d 
upper_bound = 10**3


#sieve for generating primes below the upper bound of d
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

primes = sieve(upper_bound)

def length(p):
    for i in range(2,p):
        #check order modp
        if (10**i) % p ==1:
            return i
            break

allprimes = primes[3:]
longest_length = 1
d = 1 

for p in allprimes:
    if length(p) > longest_length:
        longest_length = length(p)
        d = p

print("Longest repeating decimal:",longest_length)
print("Denominator d:",d)
