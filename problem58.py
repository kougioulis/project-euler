#Project Euler Problem 58 - Spiral Primes

tic = time.time()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

list = [1]
dim = 2*7 +1
i = 0
increment = 2
primes_count = 0

while True:
    tmp = i
    while i < (tmp + 4):
        list.append(list[i] + increment)

        if is_prime(list[i] + increment):
            primes_count += 1
        i = i + 1

    percentage_primes = primes_count / (2 * len(list) + 1) * 100
    print("Current dim: " + str(dim) + ", Primes percentage: " + "{:.4f}%".format(percentage_primes))

    if percentage_primes < 10:
        print(dim)
        break

    increment = increment + 2
    dim += 2
    
tac = time.time()

print("Elapsed time: %.2f seconds" % (tac-tic))
