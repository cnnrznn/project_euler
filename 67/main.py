#!/usr/bin/python

# solution to Project Euler problem 18
# TODO print route

import sys

def greatest_descent(pyramid, dyn, i, j):
    if i==len(pyramid)-1: # at a leaf node
        return pyramid[i][j]

    left = -1
    if dyn[i+1][j] > 0:
        left = dyn[i+1][j]
    else:
        left = greatest_descent(pyramid, dyn, i+1, j)
        dyn[i+1][j] = left

    right = greatest_descent(pyramid, dyn, i+1, j+1)
    dyn[i+1][j+1] = right

    if left > right:
        return left + pyramid[i][j]
    else:
        return right + pyramid[i][j]

# read triangle as
# [
# [x1],
# [x2, x3],
# [x4, x5],
# etc.
pyramid = []
with sys.stdin as stdin:
    lines = stdin.readlines()
    for line in lines:
        line = line.strip('\n').split()
        for i in xrange(len(line)):
            line[i] = int(line[i])
        pyramid.append(line)

# dynamic programming matrix
dyn = [[-1 for col in row] for row in pyramid]

print greatest_descent(pyramid, dyn, 0, 0)
