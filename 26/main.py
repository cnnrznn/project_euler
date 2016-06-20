#!/usr/bin/python

# Solution to Project Euler #26

_NOREPEAT = -1

win_n = 6
win_i = 7

def dec_repeat(d):
    remainders = [1]
    currRem = 1

    for arb in xrange(1000000):
        while currRem < d:
            currRem *= 10
        currRem = currRem % d
        if currRem == 0:
            return _NOREPEAT
        if currRem in remainders:
            i = remainders.index(currRem)
            return len(remainders) - i
        else:
            remainders.append(currRem)

    return _NOREPEAT

for i in xrange(7, 1000):
    n = dec_repeat(i)
    print i, n
    if n > win_n:
        win_n = n
        win_i = i
print

print win_i, win_n
print 1.0 / win_i
