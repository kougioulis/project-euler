#Trial-division primality test

def isprime(n):
    if n <=1:
        return False
    elif n==2 or n==3:
        return True
    if n % 2 == 0:
        return False
    else:
        for d in range(2,int(n**0.5) +1):
            if n%d == 0:
                return False
                break
    return True
