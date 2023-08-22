import sympy

# Sieve of Eratosthenes from Problem 10
def sieve(n):
    sieve_list = [True]*n
    for i in range(2, int(n**0.5 + 1)):
        if sieve_list[i] == True:
            for j in range(i*i, n, i):
                sieve_list[j] = False

    final = []
    for i in range(2, n):
        if sieve_list[i] ==True:
            final.append(i)
    return final

def num_rot(x):
    rot_list = []
    for i in range(len(str(x))):
        rot_list.append(sympy.isprime(int(str(x)[i: ] + str(x)[ :i])))
    return rot_list


n = 10**6
primes = sieve(n)
circular_count = 0

for i in range(0,len(primes)):
    if all(num_rot(primes[i]):
        circular_count += 1

#Sample input: 100
#Sample output: 13

print(circular_count)
