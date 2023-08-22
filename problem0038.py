#Project Euler Problem 38 - Pandigital multiples

import time

tic = time.time()

def is_pandigital(n):
    return sorted(str(n)) == [str(i) for i in range(1, 10)]

maximum_pandig = 0

for num in range(1, 10**5):
    concat = ''
    n = 1
    while len(concat) < 9:
        concat += str(num * n)
        n += 1

    if is_pandigital(concat) and len(concat) == 9:
        maximum_pandig = max(maximum_pandig, int(concat))

print(maximum_pandig)

tac = time.time()

print("Elapsed time: %.2f seconds" % (tac - tic))