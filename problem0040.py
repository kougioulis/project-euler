
string = '';
total = 1; #Champernowne's constant

for i in range(1,1000001):
    string = string + str(i) #string concatenation

n=1
while n <= 100000:
    total = total*int(string[n-1])
    n=10*n

print(total)
