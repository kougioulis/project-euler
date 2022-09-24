#Collatz sequence

def collatz(n):
    seq= []
    while n>1:
        if n%2 == 0:
            n = n/2
            seq.append(int(n))
        else:
            n = 3*n + 1
            seq.append(int(n))
    return seq

def collatz_count(n):
    count=1
    while n>1:
        count +=1
        if n%2 ==0:
            n=n/2
        else:
            n=3*n +1
    return count;

max_num = 1
chain_length = 1

for i in range(1000000):
    if collatz_count(i) > max_num:
        max_num = i
        chain_length = collatz_count(i)


print(max_num)
print(chain_length)
