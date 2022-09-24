total = 0 
for i in range(10, 355000):
    s = [pow(int(j),5) for j in str(i)] #calculate fifth powers of the digits
    if sum(s) == i: 
        total +=i

print(total)
