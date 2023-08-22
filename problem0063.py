n=10

#total_numbers = []
total = 0
def number_of_digits(num):
    digits=0
    while (num > 0):
        num = num//10
        digits = digits + 1
    return digits

for i in range(1,n+1):
    for j in range(1,n+1):
        if number_of_digits(i**j) == j:
            total = total +1

print(total)
#print(len(total_numbers))
