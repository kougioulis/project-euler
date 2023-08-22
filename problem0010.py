# Sieve of Eratosthenes of Cyrene
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


#sum of primes below two million

print(sum(sieve(2*10**6)))

