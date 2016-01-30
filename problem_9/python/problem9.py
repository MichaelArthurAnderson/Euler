# https://projecteuler.net/problem=9

import time
import math

start = time.time()

for a in range(1,999):

    for b in range(a, (999 - a) / 2):

        c = math.sqrt(a**2 + b**2)

        if a + b + c == 1000:
            answer = a * b * c
            break

    else:
        continue
    break

print "Time :",time.time() - start
print "Answer :",answer
