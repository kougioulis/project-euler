#Project Euler Problem 91 - right triangles with integer coordinates

import time

tic = time.time()

def is_right_triangle(a_squared, b_squared, c_squared): 
    sides = [a_squared, b_squared, c_squared]
    sides.sort()
    return sides[0] + sides[1] == sides[2] # use the pythagorean theorem

#generate all integer points in the grid
def right_triangle_count(limit):
    points = [(x, y) for y in range(1, limit + 1) for x in range(1, limit + 1)]
    
    count = 0
    for idx, B in enumerate(points):
        for C in points[idx + 1:]:
            if is_right_triangle(B[0]**2 + B[1]**2, C[0]**2 + C[1]**2,
                                 (B[0]-C[0])**2 + (B[1]-C[1])**2):
                count += 1
    return count

N = 50
print(right_triangle_count(N))

tac = time.time()

print("Elapsed time: %.2f seconds" %(tac - tic))

