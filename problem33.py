#Project Euler Problem #33 - Digit Cancelling Fractions

import fractions as f

prod = 1

for num in range(10, 10**2):
    for denom in range(num+1, 10**2):
        if num % 10 == 0 or denom % 10 == 0: #negligible case
            continue
            
        frac = f.Fraction(num, denom)
        cancelled_frac = f.Fraction(num // 10, denom % 10)

        if frac == cancelled_frac and frac < 1:
            prod *= frac

prod = prod.limit_denominator()
print(prod.denominator)
