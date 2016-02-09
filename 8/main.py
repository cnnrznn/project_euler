#!/usr/bin/python

inf = open("big_number")
number_lines = inf.readlines()
inf.close()

number = ""

for i in xrange(len(number_lines)):
    number_lines[i] = number_lines[i].strip('\n')
    for j in xrange(len(number_lines[i])):
        number += number_lines[i][j]

number = [int(x) for x in number]

window = 13

prods = []

for i in xrange(len(number) - (window-1)):
    tmp = number[i:i+window]
    product = 1
    for j in xrange(len(tmp)):
        product *= tmp[j]
    prods.append(product)

print max(prods)
