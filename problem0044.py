#Project Euler Problem 44 - Pentagon Numbers

import time

tic = time.time()

def pentagonal(n):
    return n * (3 * n - 1) // 2

def is_pentagonal(n):
    return ((24 * n + 1) ** 0.5 + 1) % 6 == 0

D = float('inf')

i = 1
while True:
    pent_i = pentagonal(i)
    for j in range(i - 1, 0, -1):
        pent_j = pentagonal(j)
        diff = pent_i - pent_j
        if diff >= D:
            break
        if is_pentagonal(diff) and is_pentagonal(pent_i + pent_j):
            D = diff
            break
    else:
        i += 1
        continue
    break
print("Minimum difference:", D)

tac = time.time()
print("Elapsed time: %.2f seconds" % (tac - tic))
