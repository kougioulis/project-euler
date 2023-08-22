def pal(n):
    return int(str(n)[::-1])

def is_pal(n):
    if n == pal(n):
        return True
    else:
        return False

def lychrel_check(n):
    if is_pal(n):
        return False
    i=1
    while(i<50):
        exp = n + pal(n)
        if is_pal(exp):
            return False
            break
        else:
            n = exp
            i+=1
    return True

# sample input: 47, 349, 4994
# sample output:True, True, False

conjectured_lychrel_nums = []
for i in range(1,10**4):
    if lychrel_check(i):
        conjectured_lychrel_nums.append(i)

print(len(conjectured_lychrel_nums))
