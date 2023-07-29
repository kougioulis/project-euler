#Project Euler Problem 43 - Sub-string divisibility

import time
from itertools import permutations

tic = time.time()

perms = permutations("0123456789")

s = 0
for num in perms:
    str_num = "".join(num)
    if int(str_num[1:4]) % 2 == 0 and int(str_num[2:5]) % 3 == 0 and int(str_num[3:6]) % 5 == 0 and int(str_num[4:7]) % 7 == 0 and int(str_num[5:8]) % 11 == 0 and int(str_num[6:9]) % 13 == 0 and int(str_num[7:10]) % 17 == 0:
        s += int(str_num)

print(s)

tac = time.time()

print("Elapsed time: %.2f seconds" % (tac-tic))