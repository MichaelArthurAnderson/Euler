# https://projecteuler.net/problem=6

import math
import time

start = time.time()

numbers = range(1,101)

sum_square = reduce(lambda x, y: x+(y*y), numbers)

summed = reduce(lambda x, y: x+y, numbers)

answer = (summed * summed) - sum_square

print "Time :",time.time() - start
print "Answer :",answer
