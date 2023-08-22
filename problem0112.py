#Project Euler Problem 112 - Bouncy Numbers

import time

tic = time.time()

def is_not_bouncy(n):
    if n < 100:
        return True 
    else:
        increasing, decreasing = False, False
        prev_digit = n % 10
        n = n // 10
        while n > 0:
            digit = n % 10
            if prev_digit > digit:
                decreasing = True
            elif prev_digit < digit:
                increasing = True
            if increasing and decreasing:
                return False
            prev_digit = digit
            n = n // 10
        return True
        
def is_bouncy(n):
    return not is_not_bouncy(n)

least_num = 100
bouncy_count = 0
ratio = 0
while ratio != 0.99:
    least_num += 1
    if is_bouncy(least_num):
        bouncy_count += 1
    ratio = bouncy_count / least_num

print(least_num)

tac = time.time()

print("Elapsed time: %.2f seconds" % (tac-tic))
