def pentagonal(n):
    return n*(3*n -1)//2

#since P_n = n(3n -1)/2 it is adequate to check whether 
#sqrt(24 P_n) +1) +1)//6 is a natural number
def is_pentagonal(n):
    k = ((24*n+1)**0.5 +1)/6
    return k.is_integer()

def first_n_pentagonals(n):
    pentagonals = [];
    for n in range(1,N+1):
        pentagonals.append(n*(3*n -1)//2)
    return pentagonals[0:N]

tmp=-1
minimum=500000000
index_j=-1
index_k=-1

for j in range(1,5000):
    for k in range(2,5000):
        if is_pentagonal(pentagonal(j) + pentagonal(k)):
                if is_pentagonal(abs(pentagonal(k) - pentagonal(j))):
                    D = abs(pentagonal(j) - pentagonal(k))
                    if D < minimum:
                        minimum = D
                        index_j = j
                        index_k = k

print("P_j: ",pentagonal(j))
print("P_k: ",pentagonal(k))
print("Minimum value of D: ",minimum)
