#Project Euler Problem 22 - Names Scores

import time

tic = time.time()

filename = "0022_names.txt"

def names_score(names):
    score = 0
    for name in names:
        score += ord(name) - 64 #ord('A') = 65
    return score

with open(filename) as f:
    names = f.read().replace('"','').split(',')
    names.sort()

    total_score = 0
    for i, name in enumerate(names):
        total_score += (i+1) * names_score(name)

    print(total_score)
    f.close()
    
tac = time.time()

print("Elapsed time: %.2f seconds" % (tac-tic))
