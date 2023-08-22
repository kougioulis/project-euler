#Project Euler Problem 41 - Pandigital Prime

import time

tic = time.time()

def sieve(n):
    sieve_list = [True] * (n + 1)
    sieve_list[0] = sieve_list[1] = False

    for i in range(2, int(n**0.5) + 1):
        if sieve_list[i]:
            for j in range(i * i, n + 1, i):
                sieve_list[j] = False

    primes = {num for num in range(n + 1) if sieve_list[num]}
    return primes

def is_pandigital(n, m):
    digits = 0
    while n > 0:
        digit = n % 10
        if digit == 0 or digit > m or digits & (1 << digit):
            return False
        digits |= 1 << digit
        n //= 10
    return digits == (1 << (m + 1)) - 2

def generate_pandigitals(m):
    digits = "987654321"[:m]
    num = int(''.join(digits))
    while num > 0:
        yield num
        num -= 1

# Precompute primes up to 31426 (the square root of the largest pandigital number)
primes = sieve(31426)

largest_pandigital_prime = 0
for num in generate_pandigitals(9):
    if num in primes:
        largest_pandigital_prime = num
        break

print("The largest n-pandigital prime is %d" % largest_pandigital_prime)

tac = time.time()

print("Elapsed time: %.2f seconds" % (tac - tic))

