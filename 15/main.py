#!/usr/bin/python

import sys

def count_moves(n):
    # set up grid
    grid = [[0 for i in xrange(n)] for i in xrange(n)]
    for i in xrange(n):
        grid[i][-1] = n + 1 - i
    for j in xrange(n):
        grid[-1][j] = n + 1 - j

    # calculate inner elements
    for i in xrange(n-2, -1, -1):
        for j in xrange(n-2, -1, -1):
            grid[i][j] += grid[i+1][j]
            grid[i][j] += grid[i][j+1]

    return grid[0][0]

print count_moves(int(sys.argv[1]))
