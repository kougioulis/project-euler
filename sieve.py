# Sieve of Eratosthenes of Cyrene
def sieve(n):
    sieve_list = [True]*(n+1) #boolean list of length n to keep track of the sieve
    for i in range(2, int(n**0.5 + 1)):
        if sieve_list[i] == True:
            for j in range(i*i, n+1, i): #start crossing out from the sieve
                sieve_list[j] = False
   
    primes = []
    for i in range(2, n):
        if sieve_list[i] ==True: #if not crossed out then prime
            primes.append(i)
    return primes

