#Project Euler Problem 92 - Square Digit Chains

import time
import numpy

tic = time.time()

eighty_one_count = 0

for i in range(1, 10**7):
    num = i
    while num != 1 and num != 89:
        num = sum([int(x)**2 for x in str(num)])
        if num == 89:
            eighty_one_count +=1
            break

print("The number of numbers below 10^7 that end in 89 is: " + str(eighty_one_count))

tac = time.time()

print("Elapsed time: %.2f seconds" % (tac - tic))