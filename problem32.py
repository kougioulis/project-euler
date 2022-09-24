def is_pandigital(num):
    num = [digit for digit in str(num)]
    num = sorted(num)
    for i in range(len(num)):
        if int(num[i]) != (i + 1):
            return False
    return True


prod = set()

for i in range(1,9):
    for j in range(999,9999):
        val = int(str(i) + str(j) + str(i*j))
        if is_pandigital(int(str(i) + str(j) + str(i*j))):
                if i*j not in prod:
                   prod.add(i*j)

for i in range(9,99):
    for j in range(99,9999):
        val = int(str(i) + str(j) + str(i*j))
        if is_pandigital(int(str(i) + str(j) + str(i*j))):
            if i*j not in prod:
                prod.add(i*j)
 

print(sum(prod))
