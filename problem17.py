singles = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

dec = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

#Dynamic Programming approach
# 543 = 500 + 43 = 5*100 + 4*10 + 3 

def num_to_words(n):
    if n == 1000:
        return "onethousand"
    elif n >= 100 and n < 1000:
        if n == 100:
            return "onehundred"
        else:
            if n % 100 == 0:
                return singles[ n // 100] + "hundred"
            else:
                return singles[ n // 100] + "hundred" + "and" + num_to_words(n % 100)
    elif n >= 20 and n < 100:
        return dec[n // 10] + singles[n % 10]
    elif n < 20:
        return singles[n]

s = 0

for w in range(1,1001):
    s += len(num_to_words(w))

print(s)
