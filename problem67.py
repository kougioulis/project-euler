#Project Euler Problem 67 - Maximum path sum II

#like Problem 18, use Dynamic Programming, from the bottom row to the top row 

import time
import math

tic = time.time()

with open("0067_triangle.txt", "r") as f:
    rows = f.readlines()

T = []
for row in rows:
    T.append([int(x) for x in row.split()])

i = len(T) - 1 #begin from the bottom row
while i>=0:
    j =0
    while j <= i-1: #for each column in the row
        a = T[i][j] + T[i-1][j] #sum of curr and the one above to the left
        b = T[i][j+1] + T[i-1][j] #sum of curr and the one above to the right
        if a > b:
            T[i-1][j] = a #maximum so far
        else:
            T[i-1][j] = b 
        j+=1 #move to the next column
    i -=1 #move up one row

print(T[0][0])

tac = time.time()

print("Elapsed time: %.2f seconds" % (tac - tic))
