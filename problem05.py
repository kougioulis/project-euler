def gcd(a,b):
    while a !=0:
        c = a
        a = b % a
        b = c
    return b

def lcm(a,b):
    return (a*b)/gcd(a,b)


num = 1
for i in range(2,20):
    num = int(lcm(num,i))

print(num)
