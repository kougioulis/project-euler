# Solving the diophantine equation (b/n)*(b-1/n-1) = 1/2
# This simplifies to 2b^2 - n^2 -2b + n = 0 

#(b,n)
solutions = [15,21]

while n < 10**12:
  
   b = 3*solutions[0] + 2*solutions[1] -2
   n = 4*solutions[0] + 3*solutions[1] -3

   solutions[0] = b
   solutions[1] = n


r = solutions[1] - solutions[0]
print(solutions[0])
