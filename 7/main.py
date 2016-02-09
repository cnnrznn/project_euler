#!/usr/bin/python

inf = open("primes1.txt")

inf.readline()

counter = 0
prime = -1

def find_prime():
    global inf
    global counter
    global prime

    while True:
        line = inf.readline().split()
        for i in range(len(line)):
            counter += 1
            prime = line[i]
            if counter == 10001:
                return
find_prime()

print counter, prime
