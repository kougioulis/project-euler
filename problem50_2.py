# Sieve of Erotosthenes
# One of the best algorithm to generate prime numbers
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def sieve(n):
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    # even numbers except 2 have been eliminated
    for i in range(3, int(n**0.5+1)+1, 2):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    prime = [2]
    for i in range(3, n+1, 2):
        if is_prime[i]:
            prime.append(i)
    return prime

# prime numbers upto 1 million
primes = sieve(15)

# length of the consecutive prime sum
length = 0

# value of the consecutive prime sum
largest = 0

# max value of the j variable(second for loop)
lastj = len(primes)

# two for loops
for i in range(len(primes)):
    for j in range(i+length, lastj+1):
        sol = sum(primes[i:j])
        if sol < 15:
            if sol in primes:
                length = j-i
                largest = sol
        else:
            lastj = j+1
            break

# printing the requried solution
print(largest)
