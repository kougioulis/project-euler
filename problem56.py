maximum = -1

for a in range(2,100):
    for b in range(2,100):
        exp = str(a**b)
        digit_sum = sum(int(digit) for digit in str(exp))
        if digit_sum > maximum:
            maximum = digit_sum

print("Maximum digit sum:",maximum)
