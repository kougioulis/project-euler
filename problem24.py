#Project Euler Problem 24 - Lexicographic permutations

from itertools import permutations
import time

tic = time.time()

def Problem24():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    perm = list(permutations(digits))[999999]
    return int(''.join(str(digit) for digit in perm))

print(Problem24())

tac = time.time()

print("Elapsed time: %.2f seconds" % (tac - tic))
