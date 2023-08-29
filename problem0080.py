#Project Euler Problem 80 - Square root digital expansion

import time
from decimal import Decimal, getcontext

tic = time.time()

count, N = 0, 100

getcontext().prec = 102 #set the precision to 100 digits plus the decimal point and the integer part

for i in range(1, N+1):
    sqrt_i = Decimal(i).sqrt()
    if sqrt_i != int(sqrt_i): #number is irrational
        dec = str(sqrt_i).replace('.', '')[:100] 
        count += sum([int(j) for j in dec])

print(count)

tac = time.time()

print("Elapsed time: %.2f seconds" % (tac - tic))
