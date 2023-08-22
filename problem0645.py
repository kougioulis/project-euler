import random
import statistics

import time

def Expected(D):
    emperors = 0
    holidays = set()
    while D > len(holidays):
        emperors += 1
        bday = random.choice(range(D))
        if bday not in holidays:
            holidays.add(bday)
            if (bday+2) % D in holidays:
                holidays.add((bday+1) % D)
            if (bday-2) % D in holidays:
                holidays.add((bday-1) % D)
    return emperors

t0 = time.time()

#sample inputs: D = 2, 5, 365
#sample outputs: E(D) = 1, 31/6, 1174.3501

#resampling 500 times
print(statistics.mean(Expected(10**4) for i in range(500)))

t1 = time.time()
print("-- %s seconds --" % (t1 - t0))
