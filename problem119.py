import time

def digits_sum(n):
    return sum(int(digit) for digit in str(n))


start_time = time.time()

seq=[]
n = 2
lim=30

while len(seq) < lim+1:
    for e in range(2,20):
        if digits_sum(n**e) == n:
            seq.append(n**e)
            break
    n += 1

#Sample inputs: 2, 10
#Sample outputs: 512, 614656

print(sorted(seq)[lim-1])

print("- %seconds" % (time.time() - start_time))
