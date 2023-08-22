#Project Euler Problem 81 - Path sum: two ways

import time
import numpy as np

tic = time.time()

with open("0081_matrix.txt") as f:
    lines = f.readlines()
    matrix = np.array([[int(x) for x in line.split(",")] for line in lines])
 
#use dynamic programming to solve this problem from front to back
#T[i,j] denotes the minimal path sum from [0,0] (top left) to [i,j]

T = np.zeros((80,80))
T[0,0] = matrix[0,0]

for i in range(1,80):
    T[i,0] = T[i-1,0] + matrix[i,0]

for j in range(1,80):
    T[0,j] = T[0,j-1] + matrix[0,j]
    
for i in range(1,80):
    for j in range(1,80):
        T[i, j] = min(T[i-1,j], T[i,j-1]) + matrix[i,j]

print("Minimal path sum: %d" % T[79,79])

tac = time.time()

print("Elapsed Time: %.2f seconds" % (tac-tic))