#Project Euler Problem 96 - Su Doku

import time 

from constraint import Problem, BacktrackingSolver, AllDifferentConstraint

tic = time.time()

class Problem96:
    def __init__(self, file):
        self.file = file
        self.puzzles = self.read_puzzles()
        self.solutions = self.solve_all(self.puzzles)

    def read_puzzles(self):
        puzzles = []
        with open(self.file, "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines),10): 
                puzzle = [list(map(int, line.strip())) for line in lines[i + 1 : i + 10]]
                puzzles.append(puzzle)
        return puzzles
    
    def solve_sudoku(self, puzzle):
        problem = Problem(BacktrackingSolver()) #backtracking solver on the CSP

        cols, rows = range(9), range(9)
        nums = range(1, 10)

        #specify the variables and their domains
        for i in cols:
            for j in rows:
                problem.addVariable((i, j), nums if puzzle[i][j] == 0 else [puzzle[i][j]])

        #add the constraints
        for i in cols:
            problem.addConstraint(AllDifferentConstraint(), [(i, j) for j in rows])

        for j in rows:
            problem.addConstraint(AllDifferentConstraint(), [(i, j) for i in cols])

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid = [(i + x, j + y) for x in range(3) for y in range(3)]
                problem.addConstraint(AllDifferentConstraint(), subgrid)

        solutions = problem.getSolutions()

        if len(solutions) == 1: #unique solution
            for i in cols:
                for j in rows:
                    puzzle[i][j] = solutions[0][(i, j)]
            return True
        else:
            return False
 
    def get_top_left_row(self, puzzle):
        return puzzle[0][:3]
    
    def get_top_left_subgrid(self, puzzle):
        return [puzzle[i][j] for i in range(3) for j in range(3)]
        
    '''
    #Implementation without modeling the problem as a CSP

    def find_empty_cell(self, puzzle):
        for i in range(9): #exhaustive search
            for j in range(9):
                if puzzle[i][j] == 0:
                    return i, j
        return None
    
    def is_valid_move(self, puzzle, row, col, num):
        #check whether placing num in (row, col) is valid
        for i in range(9):
            if puzzle[row][i] == num or puzzle[i][col] == num:
                return False
        #checking validity of num in the 3x3 subgrid
        starting_row = 3 * (row // 3)
        starting_col = 3 * (col // 3) 
        for i in range(3):
            for j in range(3):
                if puzzle[starting_row + i][starting_col + j] == num:
                    return False
        return True            

    def solve_sudoku(self, puzzle):       

        empty_cell = self.find_empty_cell(puzzle)
        if not empty_cell:
            return True #puzzle is solved
        empty_row, empty_col = empty_cell
        for num in range(1, 10):
            if self.is_valid_move(puzzle, empty_row, empty_col, num):
                puzzle[empty_row][empty_col] = num
                if self.solve_sudoku(puzzle):
                    return True
                #backtracking step - if the puzzle is not solved, reset the cell to 0
                puzzle[empty_row][empty_col] = 0
        return False
    '''

    def solve_all(self, puzzles):
        sols = []
        for puzzle in puzzles:
            self.solve_sudoku(puzzle)
            sols.append(self.get_top_left_row(puzzle))
        return sols

file = "p096_sudoku.txt"
problem = Problem96(file)
puzzles = problem.read_puzzles()
solutions = problem.solve_all(puzzles)
top_left_rows = [problem.get_top_left_row(puzzle) for puzzle in puzzles]
summation = sum([int("".join(map(str, row))) for row in top_left_rows])
print(summation)

tac = time.time()

print("Elapsed Time: %.2f seconds" % (tac-tic))
