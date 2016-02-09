#!/usr/bin/python

import sys

### FUNCTIONS ###

def solve(n):
    # prime factorization of n
    factors = []
    t = n
    i = 2
    while i <= t:
        while t % i == 0:
            t /= i
            factors.append(i)
        i += 1
    
    # create a list of elements numbered 0->n/2
    # sieve out multiples of factors of n
    # test remaining numbers
    return factors

### SCRIPT ###

target = int(sys.argv[1])

res = 0

print solve(1000)
