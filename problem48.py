#Project Euler Problem 48 - Self Powers

import time 

tic = time.time()

s = 0
n = 1000

for i in range(1, n+1):
    term = pow(i, i, 10**10)
    s = (s + term) % 10**10
    
print("Last 10 digits of the series is: ", s)

tac = time.time()

print("Elapsed time: %.2f seconds" % (tac-tic))
