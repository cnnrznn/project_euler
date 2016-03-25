#!/usr/bin/python

# Solution to Project Euler #22

import sys
import string

data = []
with open(sys.argv[1], 'r') as inf:
    for line in inf:
        tmpl = line.strip('\n').split(',')
        for e in tmpl:
            data.append(e.strip('"'))

data.sort()

char_score = dict()
for i in xrange(len(string.ascii_uppercase)):
    char_score[string.ascii_uppercase[i]] = i+1

res = 0

for i in xrange(len(data)):
    summ = 0
    for char in data[i]:
        summ += char_score[char]
    res += summ*(i+1)

print res
