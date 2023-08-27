# Sieve of Eratosthenes of Cyrene 
def sieve(n):
    sieve_list = [True]*(n+1) #boolean list of length n to keep track of the sieve
    sieve_list[0] = sieve_list[1] = False
    for i in range(2, int(n**0.5 + 1)):
        if sieve_list[i] == True:
            for j in range(i*i, n+1, i): #start crossing out from the sieve
                sieve_list[j] = False 
    #omit from here on and return sieve_list, to return a boolean list up to n, to check whether an
    #integer k <= n is prime or not (sieve_list[k]) in O(1) time like hashing, otherwise return the list of primes up to n
    primes = []
    for i in range(2, n):
        if sieve_list[i] ==True: #if not crossed out then prime
            primes.append(i)
    return primes

