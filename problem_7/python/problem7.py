# https://projecteuler.net/problem=7

import math
import time

# Seed the array with the lower prime values else sqrt returns a very small number and
# loop breaks too soon.
primes = [1,2,3,5,7,11,13]
candidate = max(primes)

start = time.time()

while (len(primes) < 10002):

    candidate += 2

    sqrt = int(math.ceil(math.sqrt(candidate))) + 1

    for i in range(3, sqrt, 2):
        if (i != 1 and candidate % i == 0):
            break
    else:
        primes.append(candidate);

print "Time :",time.time() - start
print "Answer :",max(primes)
