def ways(n):
    tot = [1] + [0]*n #first term 1

    for i in range(1,n+1):
        for j in range (i,n+1):
            tot[j] = tot[j] + tot[j-i]

    return tot[n]


print(ways(100))
