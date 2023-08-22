#import math (for math.factorial)

#note that as 1! = 1 and 2! = 2 are not sums, they are not included.
#otherwise, the sum of all numbers would be 40733 instead of 40730
def fact(n):
    val=1
    for i in range(1,n+1):  
        val = val*i
    return val

def sum_of_fact_digits(n):
    return sum([fact(int(i)) for i in str(n)])


curious_sum = 0
curious_numbers = [];

#iterate until n=100k
for i in range(3,10**5):
    if sum_of_fact_digits(i) == i:
        curious_sum = curious_sum + i
        curious_numbers.append(i)

print("Total sum of curious numbers:",curious_sum)
print("Curious numbers:",curious_numbers)


