#Project Euler Problem 99 - Largest exponential

import math
import time

tic = time.time()

with open('0099_base_exp.txt', 'r') as f:
    lines = f.readlines()

max_line_number = 0
max_line = 0

for line in lines:
    base, exponent = map(int, line.strip().split(','))  #strip removes the whitespaces
    line_number = exponent * math.log(base)
    if line_number > max_line_number:
        max_line_number = line_number
        max_line = lines.index(line)+1

print(max_line)

tac = time.time()

print("Elapsed time: %.2f seconds" % (tac - tic))
