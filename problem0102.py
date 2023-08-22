#Project Euler Problem 102 - Triangle Containment

#See https://mathworld.wolfram.com/TriangleInterior.html

import time
import numpy as np

tic = time.time()

with open('0102_triangles.txt', "r") as f:
    lines = f.read().splitlines()
    points = []
    for line in lines:
        points.append(line.split(','))

v = [0, 0]
count = 0
for p in points:
    v_0 = [int(p[0]), int(p[1])]
    v_1 = [int(p[2]) - int(v[0]), int(p[3]) - int(v[1])]
    v_2 = [int(p[4]) - int(v[0]), int(p[5]) - int(v[1])]

    denom = np.linalg.det(np.array([[v_1[0] - v_0[0], v_2[0] - v_0[0]], [v_1[1] - v_0[1], v_2[1] - v_0[1]]]))

    alpha = np.linalg.det(np.array([[v[0] - v_0[0], v_2[0] - v_0[0]], [v[1] - v_0[1], v_2[1] - v_0[1]]])) / denom
    beta = -np.linalg.det(np.array([[v_0[0] - v_1[0], v[0] - v_1[0]], [v_0[1] - v_1[1], v[1] - v_1[1]]])) / denom

    if alpha > 0 and beta > 0 and alpha + beta < 1:
        count += 1

print(count)

tac = time.time()
print("Elapsed time: %.2f seconds" % (tac - tic))
