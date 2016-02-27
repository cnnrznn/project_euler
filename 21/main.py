#!/usr/bin/python

# Solution to Project Euler problem 21

import argparse
from math import sqrt

# find sum of proper divisors of n
def d(n):
    global args
    summ = 1
    i=2
    while i <= sqrt(n):
        if n%i == 0:
            summ += i
            if i != sqrt(n):
                summ += n/i
            if args.v:
                print n, i, n/i
        i += 1

    return summ

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("N",
                        type=int,
                        help="Find sum of amicable numbers under N"
                        )
    parser.add_argument("-v",
                        action="store_true",
                        help="Give verbose output"
                        )
    args = parser.parse_args()

    data = [0 for i in xrange(args.N)]

    # populate sums of proper divisors
    for i in xrange(2, args.N):
        data[i] = d(i)

    # find and sum amicable numbers
    summ = 0
    for i in xrange(2, args.N):
        if data[i] < args.N:
            if i != data[i] and i == data[data[i]]:
                summ += i

    if args.v:
        for elem in data:
            print elem,
        print

    print summ
