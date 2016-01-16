# https://projecteuler.net/problem=4
upper_bound = 1000
lower_bound = 100

def find_palindrone():

    largestPalindrone = 0

    for i in range(upper_bound, lower_bound, -1):
        for j in range(upper_bound, lower_bound, -1):
            num = i * j
            if str(num) == str(num)[::-1]:
                if (num > largestPalindrone):
                    largestPalindrone = num

    return largestPalindrone

print find_palindrone()
