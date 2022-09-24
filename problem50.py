from sympy import isprime

n=10**6
primes_count = 0
primes = []
i=2

while sum(primes)<n:
    if isprime(i):
        primes.append(i)
    i+=1

best_primes_seq=[]
j=len(primes)
while j!=0:
    i=0
    while i+j < len(primes)+1:
        primes_seq = primes[i:i+j]
        if sum(primes_seq)<n and isprime(sum(primes_seq)) and len(primes_seq) > len(best_primes_seq):
            best_primes_seq = primes_seq
        i+=1
    j-=1

print(sum(best_primes_seq))
