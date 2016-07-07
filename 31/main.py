#!/usr/bin/python

# Solution to Project Euler Problem #31

import math
import itertools

_coins = [200,
          100,
          50,
          20,
          10,
          5,
          2,
          1]

def comb_with_repeat(n, r):
    return math.factorial(n+r-1) / (math.factorial(r)*math.factorial(n-1))

# Strategy:
# As in binary, have "digits," one for each value of coin.
# The base 10 number in the digit indicates how many coins of that value are being used.
# Start with '1' in the 200's slot.
# Loop over possible combinations by:
#   decreasing the value in the digit
#   supplementing that value by replacing it with 'high' value coins first
#   moving digit(s) to the right
#   if at the 1's place, step to the left
#   when the value at the current digit reaches zero, move to the left
#   if returned to the top (200's) slot, all possible combinations exhausted

curr_coins = [0]*len(_coins)
curr_coins[0] = 1
curr_digit = 0
num_ways = 1

while 1:
    if curr_coins[curr_digit] == 0:
        curr_digit -= 1
        if curr_digit == 0:
            break
    else:
        #print curr_coins

        num_ways += 1
        curr_coins[curr_digit] -= 1
        target = _coins[curr_digit]
        for i in xrange(curr_digit+1, len(curr_coins)):
            target += _coins[i] * curr_coins[i]
            curr_coins[i] = 0
        curr_digit += 1

        while target != 0:
            if _coins[curr_digit] <= target:
                curr_coins[curr_digit] += 1
                target -= _coins[curr_digit]
            else:
                curr_digit += 1

        if curr_digit == len(_coins)-1:
            curr_digit -= 1

print num_ways
