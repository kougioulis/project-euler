def triangular(n):
    #n-1 summations
    count = 0
    for i in range(1,n+1):
        count += i;
    return count

def divisors_count(n):
    total = 0
    for i in range(1, (int(n**0.5))+ 1):
        if (n % i == 0):     
            if (n / i == i) :
                total += 1
            else:
                total += 2
    return total

first = -1
k=1

while divisors_count(triangular(k)) < 500:
    if triangular(k) > first:
        first = triangular(k)
    k=k+1


print(triangular(k))
