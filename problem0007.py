import math

primes=[]
candidate=2

def is_prime(n):
    if n == 2: 
        return True
    if n < 2 or n % 2 == 0: 
        return False

    return not any(n % d == 0 for d in range(3, int(n**0.5) + 1, 2))


while len(primes) <= 10001:
    if is_prime(candidate):
        primes.append(candidate)
    candidate+=1


#1001st prime
print(primes[1000])
