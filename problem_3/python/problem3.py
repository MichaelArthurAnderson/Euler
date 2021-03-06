# https://projecteuler.net/problem=3

import math

number = 600851475143

def is_prime(n):

    if n < 3:
        return True

    if n % 2 == 0:
        return False

    for x in range(2, int(math.sqrt(n)) + 1):
        if n % x == 0:
            return False

    return True

largestPrimeDivisor = number

counter = 2

while counter <= number:
    if number % counter == 0 and is_prime(counter):
        largestPrimeDivisor = counter
        number /= counter
    else:
        counter += 1

print largestPrimeDivisor
