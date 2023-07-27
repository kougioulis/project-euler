#Project Euler Problem 107 - Minimal Network

import time, random, heapq 

tic = time.time()

with open("0107_network.txt", "r") as file:
    lines = file.readlines() #line split

adjacency_matrix = []

for line in lines:
    weights = line.strip().split(",")
    row = [int(w) if w != "-" else 0 for w in weights]
    adjacency_matrix.append(row)

def Prim_MST(adjacency_matrix):
    vertices = [i for i in range(len(adjacency_matrix))]
    num_vertices = len(vertices)
    start = random.choice(vertices)

    D = [float("inf") for _ in range(num_vertices)]
    D[start] = 0

    #init the MST as an empty set
    MST = set()

    #init the priority queue with the start vertex and its distance
    Q = [(0, start)]

    while Q:
        (u, e) = heapq.heappop(Q)  # Use heapq to get the minimum element efficiently

        if e not in MST:
            MST.add(e)
            for v in range(num_vertices):
                if adjacency_matrix[e][v] > 0 and v not in MST: #for each vertex v adjacent to e
                    if adjacency_matrix[e][v] < D[v]:  #perform relaxation on edge (e, v)
                        D[v] = adjacency_matrix[e][v]
                        heapq.heappush(Q, (D[v], v))  # push the updated distance and vertex pair to the priority queue

    return sum(D)

answer = sum(sum(row) for row in adjacency_matrix) // 2 - Prim_MST(adjacency_matrix)

print(answer)

tac = time.time()

print("Elapsed time: %.2f seconds" % (tac - tic))