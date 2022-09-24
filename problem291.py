from sympy import isprime


def is_panataipol(p):

    for x in range(1,20*p):
        for y in range(1,x):
            num = x**4 - y**4
            den = x**3 - y**3
            p = num/den
            if isprime(p):
                print(num/den)

#the Panaitopol prime sequence is equivalent to primes of the form
# j^2 + (j+1)^2 with j \in \mathbb{N}

bound = 5*10**6
max_panataipol_prime = -1

for j in range(1,bound):
    p = j**2 + (j+1)**2
    if isprime(p):
        if p > bound:
            break;
        max_panataipol_prime = p

print(max_panataipol_prime)


