#!/usr/bin/python

import multiprocessing
from multiprocessing import Pool

def collatz(n):
    num = n
    res = 0
    while n != 1:
        if n%2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        res += 1

    return num, res

p = Pool(multiprocessing.cpu_count())

ops = xrange(1, 1000000)

res = p.map(collatz, ops)

print max(res, key=lambda tup: tup[1])
