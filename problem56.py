#Project Euler Problem 56 - Powerful digit sum

import time

tic = time.time()

print("Maximum Digit Sum:",max(sum(int(digit) for digit in str(a**b)) for a in range(90,100) for b in range(90,100)))
      
tac = time.time()

print("Elapsed time: %.2f seconds" % (tac-tic))
