#Project Euler Problem 28 - Number Spiral Diagonals

import time

tic = time.time()

list = [1]
dim=1001
i=0
increment=2

while len(list) < 2*dim -1: #number of elements in the left and right diagonals
    tmp=i
    while (i < (tmp+ 4)): #add 4 elements to the list
        list.append(list[i]+increment)
        i= i+1
    increment = increment+2 #increment by 2 for each new layer
        
print(sum(list))

tac = time.time()
