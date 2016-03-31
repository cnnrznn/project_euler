#!/usr/bin/python

# Solution to Project Euler #23

from math import sqrt
import time

def prop_div(n):
    divs = [1]
    for i in xrange(2, int(sqrt(n))+1):
        if n%i == 0:
            divs.append(i)
            if i != sqrt(n):
                divs.append(n/i)

    return divs

sum_abund = [0 for i in xrange(28124)] # 1=abundant number
abund = []

start = time.clock()

for i in xrange(1, len(sum_abund)):
    if sum(prop_div(i)) > i:
        abund.append(i)
        for j in xrange(len(abund)):
            try:
                sum_abund[i + abund[j]] = 1
            except IndexError:
                pass

summ = 0

for i in xrange(len(sum_abund)):
    if not sum_abund[i]:
        summ += i

end = time.clock()


print summ, end-start
