def gcd(a,b):
    while b !=0:
        rem = a % b
        a = b
        b = rem
    return a

def lcm(a,b):
    return (a*b)/gcd(a,b)

num = 1
for i in range(2,20):
    num = int(lcm(num,i))

print(num)
