#Project Euler Problem 85 - Counting rectangles

import time

tic = time.time()

def rectangles_count(n, m):
    return (n*(n+1)*m*(m+1)) // 4 # \binom{n+1}{2} * \binom{m+1}{2}

N = 2*10**6
sup = float('inf')

for n in range(1, 5000):  
    for m in range(n, 5000): 
        count = rectangles_count(n, m)
        distance = abs(count - N)
        if distance < sup:
            sup = distance
            area = n*m
        if count > N:
            break

print(area)

tac = time.time()

print("Elapsed time: %.2f seconds" % (tac-tic))
