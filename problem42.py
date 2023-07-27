#Project Euler Problem 42 - Coded Triangle Numbers

import time

tic = time.time()

with open('0042_words.txt') as file:
    words = file.read().replace('"', '').split(',')
    words.sort()

max_word_len = len(words[-1])
max_word_value = max_word_len * 26

def compute_triangle_numbers(n):
    triangle_numbers = []
    for i in range(1, n + 1):
        triangle_numbers.append(int((i * (i + 1)) / 2))
    return triangle_numbers

#compute triangle numbers up to max_word_value
triangle_numbers = compute_triangle_numbers(max_word_value)

c = 0 
triangle_words = set()
for word in words:
    word_value = 0
    for letter in word:
        word_value += ord(letter) - 64
    if word_value in triangle_numbers:
        c += 1
        triangle_words.add(word)

print("The number of triangle words is:", c)
print("The triangle words are:", triangle_words)

tac = time.time()

print("Elapsed time: %.2f seconds" % (tac - tic))