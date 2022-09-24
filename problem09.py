n = 1000

found = False
pyth_triplet = []
a=0
b=0

#c = sqrt(a^2 + b^2 so reduce from three to two degrees of freedom
while a < n and found == False:
    a = a +1
    b = 0
    while b < n and found == False:
        b = b +1
        c = (a**2 + b**2)**0.5
        if (a+b+c) == n:
            found = True
            pyth_triplet.append(a)
            pyth_triplet.append(b)
            pyth_triplet.append(c)
            break

print(pyth_triplet[0]*pyth_triplet[1]*pyth_triplet[2])
