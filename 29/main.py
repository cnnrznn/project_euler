#!/usr/bin/python

# Solution to Project Euler Problem #29

terms = dict()

for a in xrange(2, 101):
    for b in xrange(2, 101):
        terms[a**b] = 0

print len(terms.keys())
