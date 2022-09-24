from sympy import *
import numpy

def left_truncatable():
    lst = [2,3,5,7] #by truncating left, the final rightmost digit must be prime
    left_truncatable_primes = []
    while len(lst) != 0:
        tmp = lst.pop(0)
        for y in [1,3,5,7,9]: #primes >2 are odd
            left_truncated  = int(str(tmp) + str(y))
            if isprime(left_truncated):
                lst.append(left_truncated)
                left_truncatable_primes.append(left_truncated)
    return left_truncatable_primes

def right_truncatable():
    lst = [2,3,5,7] #by truncating right, the final leftmost digit must be prime
    right_truncatable_primes = []
    while len(lst) != 0:
        tmp = lst.pop(0)
        for y in [1,2,3,4,5,6,7,8,9]: #any digits to the left is possible
            right_truncated = int(str(y) + str(tmp))
            if isprime(right_truncated):
                lst.append(right_truncated)
                right_truncatable_primes.append(right_truncated)
    return right_truncatable_primes


#common elements of both lists using numpy
left_and_right_truncatable = numpy.intersect1d(left_truncatable(),
        right_truncatable())

#Pythonic way using the intersection function
#left_and_right_truncatable = set(left_truncatable()).intersection(right_truncatable())

print(sum(left_and_right_truncatable))

