#!/usr/bin/python

# Solution to Project Euler Problem #30

summ = 0

for i in xrange(2, 1000000):
    si = str(i)
    lsum = 0
    for c in si:
        lsum += int(c)**5
    if lsum == i:
        print i
        summ += i

print summ
