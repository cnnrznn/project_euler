#!/usr/bin/python

sum_of_squares = 0
square_of_sum = 0

for i in xrange(1, 101):
    sum_of_squares += i**2
    square_of_sum += i

square_of_sum = square_of_sum**2

print square_of_sum - sum_of_squares
