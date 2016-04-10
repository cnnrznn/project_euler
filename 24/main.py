#!/usr/bin/python

# Solution to Project Euler #24

import sys

target = int(sys.argv[1])

num_perms = [1 for i in xrange(11)]
for i in xrange(1, len(num_perms)):
    num_perms[i] = i * num_perms[i-1]

for i in xrange(len(num_perms)):
    print i, num_perms[i]
print

currdig = 1
while num_perms[currdig] < target:
    currdig += 1
#print currdig

result = []
avail_digs = [i for i in xrange(10)]

for i in xrange(10, currdig, -1):
    result.append(avail_digs.pop(0))

index = 1

while index != target:
    addend = num_perms[currdig-1]
    i = 0
    while index < target:
        index += addend
        i += 1
    if index > target:
        index -= addend
        i -= 1

    result.append(avail_digs.pop(i))
    currdig -= 1

result += avail_digs
print result
