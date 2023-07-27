#Project Euler Problem 186 

#INCOMPLETE

import time

def S(k):
    if k <= 55:
        return (100003 - 200003*k + 300007*k**3) % 10**3
    else:
        return (S(k-24) + S(k-55)) % 10**3

def Caller(n):
    return S(2*n-1)

def Called(n):
    return S(2*n)

def generate():
    caller = [Caller(i) for i in range(1, 10**3+1)]
    called = [Called(i) for i in range(1, 10**3+1)]
    return caller, called

def problem186():
    caller, called = generate()

    N = 10**3 + 1
    parent = list(range(N))
    size = [1] * N

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x, root_y = find(x), find(y)
        if root_x != root_y:
            if size[root_x] < size[root_y]:
                parent[root_x] = root_y
                size[root_y] += size[root_x]
            else:
                parent[root_y] = root_x
                size[root_x] += size[root_y]

    prime_minister = Caller(524287)  # Prime minister phone number
    num_members = 1

    for i in range(1, 10**3+1):
        if num_members > 9900:
            break
        caller_number, called_number = caller[i-1], called[i-1]
        if caller_number != called_number:
            union(caller_number, called_number)
            if find(prime_minister) == find(caller_number):
                num_members = size[find(prime_minister)]

    return num_members

tic = time.time()
result = problem186()
tac = time.time()

print("Number of members in the subtree of the Prime Minister:", result)
print("Elapsed time: %.2f seconds" % (tac-tic))
