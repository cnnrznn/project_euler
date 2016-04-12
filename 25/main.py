#!/usr/bin/python

# Solution to Project Euler #25

target_digits = 1000 # number of digits

fibold = 1
fibnew = 1
index = 2

while len(str(fibnew)) < target_digits:
    tmp = fibnew
    fibnew += fibold
    fibold = tmp
    index += 1

print index
print len(str(fibnew))
print fibnew
