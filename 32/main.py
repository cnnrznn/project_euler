#!/usr/bin/python

# Solution to Project Euler #32

import itertools

digits = [str(i) for i in xrange(1, 10)]

res = dict()

for i in xrange(1, 9):
    for tup1 in itertools.permutations(digits, i):
        #print 'tup1:', tup1
        dig = list(digits)
        for t in tup1:
            dig.remove(t)
        for j in xrange(1, 10-i):
            for tup2 in itertools.permutations(dig, j):
                target = list(dig)
                for t in tup2:
                    target.remove(t)
                #print 'tup2:', tup2
                f1 = int(''.join(tup1))
                f2 = int(''.join(tup2))
                prod = f1 * f2
                #print
                try:
                    prodtmp = list(str(prod))
                    for p in prodtmp:
                        target.remove(p)
                    if len(target) == 0:
                        #print prod, target
                        res[prod] = 1
                except:
                    pass

summ = 0
for key in res:
    summ += key
print res
print summ
