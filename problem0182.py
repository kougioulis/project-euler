import math 

#input: list of prime factors of n (\phi(pq) = \phi(p)*\phi(q)
def phi(p,q):
    return (p -1)*(q - 1)

p = 1009
q = 3643

print(phi(n))

enc_candidates = []
#candidate encryption keys, the ones coprime to phi(n)
for e in range(1,phi(n)):
    if math.gcd(e,phi(n))==1:
        enc_candidates.append(e)

# The uncocealed messages m with encryption key e are those satisfying 
# m^e = m mod n
#It can be shown that the total number of solutions to m^e = m modp is 
# (e-1,p-1) + 1 modp (Exercise)
# Similarly (e-1,p-1) + 1 modq for m^e = m modq
# Because n=pq, it can be shown that the total number of unconcealed
# messages is (1 + (e-1,p-1))*(1 + (e-1,q-1))modn

#we are searching for key e with minimum unconcealed messages

best_candidate = 10**8 #an upper bound
total = 0 

for e in range(0,phi(p,q)):
    sols_num = math.fmod((math.gcd(e-1,p-1) +1)*(math.gcd(e-1,q-1)+1),p*q)
    if best_candidate == p*q:
        total += e
    elif best_candidate > p*q:
        best_candidate = p*q
        total = e

print(total)

