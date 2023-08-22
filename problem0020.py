from math import factorial

#recall that \Gamma(n+1) = n!
#trivial with Python 

def digits(n):
    return list(int(d) for d in str(n))


total = sum(digits(factorial(100)))

print(total)

