# https://projecteuler.net/problem=5

import math
import time

start=time.time()

divisors = (11,12,13,14,15,16,17,18,19)

smallestMultiple = 19 * 20

found = False

while (not found):

    for divisor in divisors:
        if (smallestMultiple % divisor == 0):
            found = True
        else:
            found = False
            smallestMultiple += 20
            break;

print "Time :",time.time() - start
print "N :",smallestMultiple
