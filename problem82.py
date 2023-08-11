#Project Euler Problem 82: Path sum: Three ways

import time
import numpy as np

tic = time.time()

with open("0082_matrix.txt") as f:
    lines = f.readlines()
    matrix = np.array([[int(x) for x in line.split(",")] for line in lines])

rows, cols = matrix.shape

T = np.zeros((rows, cols), dtype=int)

#init the first column
T[:, 0] = matrix[:, 0]

for j in range(1, cols):
    #move right
    T[:, j] = T[:, j - 1] + matrix[:, j]
    
    for i in range(1, rows):
        #move down
        T[i, j] = min(T[i, j], T[i - 1, j] + matrix[i, j])
    
    for i in range(rows - 2, -1, -1):
        #move up
        T[i, j] = min(T[i, j], T[i + 1, j] + matrix[i, j])

#minimum of the last column
min_path_sum = min(T[i, cols - 1] for i in range(rows))

print(min_path_sum)

tac = time.time()

print("Elapsed Time: %.2f seconds" % (tac - tic))

