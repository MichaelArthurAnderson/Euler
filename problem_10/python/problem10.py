# https://projecteuler.net/problem=10

import math
import time

# Seed the array with the lower prime values else sqrt returns a very small number and
# loop breaks too soon.
primes = [2,3,5,7,11,13]
answer = sum(primes)
candidate = max(primes)

start = time.time()

while (candidate < 2000000):

    candidate += 2

    sqrt = int(math.ceil(math.sqrt(candidate))) + 1

    for i in range(3, sqrt, 2):
        if (candidate % i == 0):
            break
    else:
        answer += candidate
        print candidate, answer

print "Time :",time.time() - start
print "Answer :",answer
