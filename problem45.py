#Project Euler Problem 45 - Triangular, Pentagonal, and Hexagonal

import time

tic = time.time()

#Approach 1: Increment the index of the triangular sequence and check if the number is pentagonal and hexagonal
def triangular(n):
    return n*(n+1)//2

def is_pentagonal(p):
    n = ((24*p + 1)**0.5) % 6
    return n == 5 #pentagonal if n \equiv 5 mod 6

def is_hexagonal(h):
    n = ((8*h + 1)**0.5) % 4
    return n == 3 #hexagonal if n \equiv 3 mod 4

i = 286  #begin from the next index after 285
while True:
    t = triangular(i)
    if is_pentagonal(t) and is_hexagonal(t):
        print("The next triangular number that is also pentagonal and hexagonal is %d" % t)
        break
    i += 1

'''
#Approach 2: Increment the smallest number of the three sets (T, P, H) at each step

T, P, H = set(), set(), set()

i, j, k = 285, 165, 143
T.add(i*(i+1)//2)
P.add(j*(3*j-1)//2)
H.add(k*(2*k-1))

while True:
    i, j, k = i+1, j+1, k+1
    t, p, h = i*(i+1)//2, j*(3*j-1)//2, k*(2*k-1)

    T.add(t)
    P.add(p)
    H.add(h)        
    
    if t in P and t in H:
        print("The next triangular number that is also pentagonal and hexagonal is %d" % t)
        print("(i,j,k) = (%d,%d,%d)" % (i,j,k))
        break
    elif h <= t and h <= p:
        k += 1
    elif p <= t and p <= h:
        j += 1
    else:
        i += 1

'''
tac = time.time()

print("Elapsed time: %.5f seconds" % (tac-tic))

