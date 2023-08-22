#shares palindrome function with Problem 125

def is_pal(n):
    r = int(str(n)[::-1])
    if r == n:
        return True
    else:
        return False

# for 2 digit numbers: x*y with x,y \in \left{10,11,...,99\right\}
# results in product of length 4 
# ...
# for x with length l(x) and y with length l(y), 
# l(x*y) = l(x)*l(y)

prod = 0
max_prod = 0
num1 = 9
num2 = 9
#3 digit numbers 
for i in range(100,1000): #100 to 999 inclusive
    for j in range(100,1000): #100 to 999 inclusive
        prod = i*j
        if is_pal(prod):
            if prod > max_prod:
                max_prod = prod
                num1 = i
                num2 = j

print(max_prod)
print(num1,num2)
