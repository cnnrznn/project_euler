#!/usr/bin/python

# solution to Project Euler problem 18

import sys

def greatest_descent(pyramid, i, j):
    if i==len(pyramid)-1: # at a leaf node
        return pyramid[i][j]

    left = greatest_descent(pyramid, i+1, j)
    right = greatest_descent(pyramid, i+1, j+1)

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

print greatest_descent(pyramid, 0, 0)
