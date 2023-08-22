import time 

def is_palindrome(n):
    return n == n[::-1]


#first and last bits have to be one (for binary) so remove odd numbers
def generate_palindromes(M):
    return [x for x in range(1,M+1) if str(x)==str(x)[::-1] and x%2 ==1]
    
M = 10**6
palindromes = generate_palindromes(M)

s=0
lst=[]

#check all decimal palindromes in binary

for i in range(1,len(palindromes)):
    if is_palindrome(bin(palindromes[i])[2:]):
        lst.append(palindromes[i])
        s +=palindromes[i]


start_time = time.time()
print(s)
print(len(palindromes))
print("--- %s seconds ---" % (time.time() - start_time))
