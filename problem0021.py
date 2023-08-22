from math import sqrt

#using a similar subroutine for finding divisors like in Problem 12

#TODO: using prime factorization and multiplcative functions
def proper_divisors(n):
    total=[]
    for i in range(1, n):
        if (n % i == 0):
                total.append(i)
    return total

#TODO: using \sigma(n) function using prime factorization
def sum_of_proper_divisors(n):
    return sum(proper_divisors(n))

bound = 10000
amicable_sum = 0
factors_i = []
factors_j = []
 
for i in range(2,bound):
    factors_i = sum_of_proper_divisors(i);
    if (factors_i > i) and (factors_i <= bound):
        factors_j = sum_of_proper_divisors(factors_i)
        if factors_j == i:
            amicable_sum += i + factors_i

#sample input
print(proper_divisors(220))
print(sum_of_proper_divisors(220)) #d(220) = 284

print(amicable_sum)


