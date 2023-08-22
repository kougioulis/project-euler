
n = 100

e=[2]
i=1
while len(e) < n:
    e.append(1)
    e.append(2*i)
    e.append(1)
    i += 1  
    e = e[0:n]
    e = e[::-1]
    numerator = 1
    denominator = e[0]
    
    for x in range(1,n):
        numerator = denominator
        denominator =  e[x]*denominator + numerator
      

print(sum([int(y) for y in list(str(denominator))]))
