#Project Euler Problem 52 - Permuted Multiples

import time

tic = time.time()

smallest_num = 0
found = False

while not found:
    smallest_num +=1
    for i in range(2,7):
        if sorted(str(smallest_num)) != sorted(str(i*smallest_num)):
            break
    else:
        found = True
        print(smallest_num)

tac = time.time()

print("Elapsed Time: %.2f seconds" % (tac-tic))