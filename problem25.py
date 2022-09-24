#fibbonaci without recursion
def fibonacci(n):
    a=0
    b=1
    if n == 0:
        return 0
    else:
        for i in range(1,n):
            c = a + b
            a = b
            b = c
        return b

number = 1
term = 1
while  len(str(number)) < 3:
    number = fibonacci(term) + fibonacci(term-1)
    term+=1

print(term)
print(fibonacci(term))
