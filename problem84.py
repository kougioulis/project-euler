#Project Euler Problem 84 - Monopoly odds

import time
import random

import numpy as np

tic = time.time()

squares = [00] * 40
die_sides = 4 
consecutive_doubles = 0
doubles_limit = 3

current_position = 0

railway_squares = [5, 15, 25, 35]
utility_squares = [12, 28]

def find_next_railway(current_pos):
    for i in range(len(railway_squares)):
        if current_pos < railway_squares[i]:
            return railway_squares[i]
    return railway_squares[0]

def find_next_utility(current_pos):
    for i in range(len(utility_squares)):
        if current_pos < utility_squares[i]:
            return utility_squares[i]
    return utility_squares[0]

def go_back_n_squares(current_pos,n):
    return (current_pos - n) % 40

community_chest_cards = [00]*16
community_chest_cards[0] = 00  # Go
community_chest_cards[1] = 10  # Jail

# Put the community chest cards in a queue to simulate the deck
community_chest_cards_queue = community_chest_cards.copy()

chance_cards = [00]*16
chance_cards[0] = 00 #Go
chance_cards[1] = 10 #jail
chance_cards[2] = 11 #C1
chance_cards[3] = 24 #E3
chance_cards[4] = 39 #H2
chance_cards[5] = 5 #R1
chance_cards[6] = find_next_railway(current_position) #visit next railway
chance_cards[7] = find_next_railway(current_position) #visit next railway
chance_cards[8] = find_next_utility(current_position) #visit next utility
chance_cards[9] = go_back_n_squares(current_position,3) #go back 3 squares

chance_cards_queue = chance_cards.copy()

def roll(sides):
    return random.randint(1, sides)

#perform monte carlo simulation of the game for N turns
N = 10**8
visit_count = [0]*40

for i in range(N):
    first_die = roll(die_sides)
    second_die = roll(die_sides)

    if first_die == second_die:
        consecutive_doubles += 1
        if consecutive_doubles == doubles_limit:
            current_position = 10
            visit_count[current_position] += 1
    else:
        consecutive_doubles = 0

        current_position = (current_position + first_die + second_die) % 40

        if current_position == 30: #go to jail
            current_position = 10
            visit_count[current_position] += 1
        elif current_position in [2, 17, 33]:  #community chest
            card = community_chest_cards_queue.pop(0)
            if card != 0:
                current_position = card
            visit_count[current_position] += 1
            community_chest_cards_queue.append(card)
        elif current_position in [7, 22, 36]: #chance card
            card = chance_cards_queue.pop(0)
            if card != 0:
                current_position = card
            visit_count[current_position] += 1
            chance_cards_queue.append(card)
        else:
            visit_count[current_position] += 1

top_three = np.argsort(visit_count)[-3:]

print(str(top_three[2]) + str(top_three[1]) + str(top_three[0]))

tac = time.time()

print("Elapsed time: %.2f seconds" % (tac - tic))
