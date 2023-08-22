n=10

#sum_of_squares = 0
#for i in range(n+1): #from 0 to n - or range(1,n+1)
#    sum_of_squares = sum_of_squares + i**2

sum_of_squares = n*(n+1)*(2*n+1)//6 
squared_sum = ( n*(n+1)//2 )**2

print(squared_sum -sum_of_squares)
