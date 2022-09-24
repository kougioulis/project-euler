i=0
j=1
n=2
even_sum=0

while (n < 4000000):
    n=i+j
    i=j
    j=n
    if (n%2==0):
        even_sum += n

print(even_sum)

