#largest prime factor of n

def is_prime(n):
    if n <=1:
        return False
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
    return True

def largest_prime_factor(n):
    max_prime=1

    for i in range(2, n//2):
        if n % i == 0:
            if is_prime(i):
                if i > max_prime:
                    max_prime = i
    return max_prime

print(largest_prime_factor(600851475143))
