from sympy import divisors

abundant_numbers = []

for n in range(1,28123 + 1):
    if n < sum(divisors(n))-n:
        abundant_numbers.append(n)

check = [True]*28124

for i in range(len(abundant_numbers)):
    for j in range(len(abundant_numbers)):
        index = abundant_numbers[i] + abundant_numbers[j]
        if index < 28124:
            check[index] = False


s = sum([i for i in range(len(check)) if check[i]])

print(s)
