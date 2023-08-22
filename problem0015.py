import math 

#lattice paths from (0,0) to (n,k) is "n+k choose n" 
# according to pascals triangle
def lattice_paths(n,k):
 
    return math.factorial(n+k)//(math.factorial(n)*math.factorial(k))


grid_dim = 20

print(lattice_paths(grid_dim,grid_dim))

