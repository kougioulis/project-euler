#Project Euler Problem 313 - Sliding game

import time
import heapq

tic = time.time()

class Problem313:
    
    def create_game(self, m, n):
        state = []
        for _ in range(n):
            state.append([1]*m) #blue balls
        state[0][0] = 2 #red ball
        state[n-1][m-1] = 0 #empty tile
        return state
    
    def is_goal_state(self, state, m, n):
        return state[n-1][m-1] == 2
    
    def move_tile(self, board, x, y, action):
        pos = board[x][y]
        if action == "up":
            new_x, new_y = x - 1, y
        if action == "down":
            new_x, new_y = x + 1, y
        if action == "right":
            new_x, new_y = x, y + 1
        if action == "left":
            new_x, new_y = x, y - 1
            
        board[new_x][new_y] = pos
        board[x][y] = 0

        return board
    
    #find the neighboring tiles of the empty tile (only ones that can be moved)
    def find_movable_tiles(self, empty_x, empty_y, m, n):
        pieces = []
        if empty_x + 1 < n:
            pieces.append((empty_x + 1, empty_y, "up"))
        if empty_x - 1 >= 0:
            pieces.append((empty_x - 1, empty_y, "down"))
        if empty_y + 1 < m:
            pieces.append((empty_x, empty_y + 1, "left"))
        if empty_y - 1 >= 0:
            pieces.append((empty_x, empty_y - 1, "right"))
        return pieces
    
    #admissible heuristic => always underestimates the cost
    def manhattan(self, x_1, y_1, x_2, y_2):
        return abs(x_1 - x_2) + abs(y_1 - y_2)
    
    def bfs(self, m, n):
        frontier = []
        initial_state = (self.board, n-1, m-1, 0)  #board, empty tile position, move (cost)
        frontier.append(initial_state)
        explored = set()

        while frontier:
            (b, empty_x, empty_y, move) = frontier.pop(0)
            curr_board = str(b)
            if curr_board not in explored:
                explored.add(curr_board)
                for xx, yy, d in self.find_movable_tiles(empty_x, empty_y, m, n):
                    copy = [row[:] for row in b]  #create a copy of the board
                    new = self.move_tile(copy, xx, yy, d)
                    if self.is_goal_state(new, m, n):
                        return move + 1
                    frontier.append((new, xx, yy, move + 1))
        return float("-inf")  #no solution found
    
    def a_star(self, m, n):
        frontier = []
        initial_state = (self.board, n - 1, m - 1, 0)  # board, empty tile position, move (cost)
        frontier.append((0, initial_state))  # priority queue (priority-cost, state)
        explored = set()

        while frontier:
            _, (b, empty_x, empty_y, move) = heapq.heappop(frontier)
            curr_board = str(b)
            if curr_board not in explored:
                explored.add(curr_board)
                if self.is_goal_state(b, m, n):
                    return move + 1

                for xx, yy, d in self.find_movable_tiles(empty_x, empty_y, m, n):
                    copy = [row[:] for row in b]
                    new = self.move_tile(copy, xx, yy, d)
                    heuristic_cost = self.manhattan(xx, yy, n - 1, m - 1)
                    total_cost = move + 1 + heuristic_cost
                    heapq.heappush(frontier, (total_cost, (new, xx, yy, move + 1)))
        return float("-inf")  # Indicate no solution found
    
    def __init__(self, m, n):
        self.board = self.create_game(m, n)
        self.solution = self.bfs(m, n)
        #self.solution = self.a_star(m, n)

def sieve(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i**2, n + 1, i):
                primes[j] = False
    return primes

#closed form by observing the pattern given m and n 
def S(m, n):
    #if m == 2 and n == 2:
    #    return 5 #base case
    if n == m:
        return 8*m - 11
    return 6*n + 2*m - 13

'''
#Test cases: (m,n) = (2,2), S(m,n) = 5 and (m,n) = (5,4), S(m,n) = 5
m, n = 5, 4

s = Problem313(m, n)

print("Solution found using BFS with total steps", s.solution)

print("Number of steps using the closed form S(m, n) is", S(m,n))
'''

max_s = S(10**6, 10**6)

lim = int(max_s**0.5) + 1
primes = sieve(lim)

count = 0
for i in range(2, lim):
    for j in range(2, lim):
        s_value = S(i, j)
        if primes[int(s_value**0.5)]:
            count += 1

print("Number of grids such that S(m,n) = p^2 where p < 10^6 prime is", count)

tac = time.time()

print("Elapsed time: %.2f seconds" % (tac - tic))
