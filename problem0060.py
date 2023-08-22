from sympy import *

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

# concat x to y 
def left_concat(x,y):
    return int(str(x) + str(y))

# concat x to y to the right
def right_concat(x,y):
    return int(str(y) + str(x))

# check if left or right concatenation of primes is prime
def concat_is_prime(x,y):
    if isprime(x) and isprime(y):
        if isprime(left_concat(x,y)) and isprime(right_concat(x,y)):
            return True
        else:
            return False
    return False



primes = sieve(10**4)

# looking for lowest sum of five primes for which any two concatenate to
# produce another prime

candidates = []

# iteratively keep checking each pair of primes

first = False
second = False

for a in range(2,len(primes)):
    for b in range(a+1,len(primes)):
        if concat_is_prime(primes[a],primes[b]):
            for c in range(b+1, len(primes)):
                if concat_is_prime(primes[a],primes[c]) and concat_is_prime(primes[b],primes[c]):
                    for d in range(c+1, len(primes)):
                        if concat_is_prime(primes[a],primes[d]) and concat_is_prime(primes[b],primes[d]) and concat_is_prime(primes[c],primes[d]):
                            for e in range(d+1,len(primes)):
                                if concat_is_prime(primes[a],primes[e]) and concat_is_prime(primes[b],primes[e]) and concat_is_prime(primes[c],primes[e]) and concat_is_prime(primes[d],primes[e]):
                                    if not first and not second:
                                        num = [primes[a],primes[b],primes[c],
                                                primes[d],primes[e]]
                                        candidates.append(sum(num))
                                        first = False
                                    else:
                                        second = True
                                        break


candidates = sorted(candidates)
print(candidates[0])
