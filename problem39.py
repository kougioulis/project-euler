#Project Euler Problem #39 - Integer Right Triangles

import time

tic = time.time()

perims = []

for a in range(1, 500):
    for b in range(a, 500):
        c = (a**2 + b**2)**0.5
        if int(c) == c and a + b + c <= 1000:
            perims.append(a+b+c)

print(max(set(perims), key=perims.count))

tac = time.time()

print("Elapsed time %.2f seconds" % (tac - tic))