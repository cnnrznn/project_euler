#!/usr/bin/python

# Solution to Project Euler Problem #28

#n = 5
n = 1001

mat = [[0 for j in xrange(n)] for i in xrange(n)]
curr = n*n

# populate matrix
for i in xrange(n/2):
    col = i
    length = n - 2*i
    #print col, length

    # top
    for j in xrange(col+length-1, col-1, -1):
        #print i, j
        mat[i][j] = curr
        curr -= 1
    # left
    for k in xrange(i+1, i+length):
        #print k, col
        mat[k][col] = curr
        curr -= 1
    # bottom
    for j in xrange(col+1, col+length):
        #print i+length-1, j
        mat[i+length-1][j] = curr
        curr -= 1
    # right
    for k in xrange(i+length-2, i, -1):
        #print k, col+length-1
        mat[k][col+length-1] = curr
        curr -= 1
mat[n/2][n/2] = 1

# find sum of the diagonals
summ = 0
for i in xrange(n):
    summ += mat[i][i]
    summ += mat[i][n-1-i]
summ -= 1 # double counted 1
print summ
