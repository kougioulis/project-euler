import math 

def is_pal(n):
    r = int(str(n)[::-1])
    if n == r:
        return True
    else:
        return False


bound = 1000;

total = 0;
num_list = []

for i in range(1, int(math.sqrt(bound))):
    num = i*i;
    for j in range(i+1, int(math.sqrt(bound))):
        num = num +j*j
        if (num > bound):
            break;
        if is_pal(num) and num not in num_list:
            total = total + num
            num_list.append(num)

print(total)
