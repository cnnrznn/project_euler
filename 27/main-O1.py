#!/usr/bin/python

# Solution to Project Euler Problem #27

def binsearch(val, arr, start, stop):
    if stop - start < 2:
        if arr[start] == val:
            return True
        else:
            return False

    mid = (start + stop) / 2

    if arr[mid] == val:
        return True

    if arr[mid] < val:
        return binsearch(val, arr, mid+1, stop)
    if arr[mid] > val:
        return binsearch(val, arr, start, mid)

_size = 10000000

# prime sieve
primes = []
is_prime = [1]*_size

for i in xrange(2, _size):
    if is_prime[i]:
        primes.append(i)
        for j in xrange(2*i, _size, i):
            is_prime[j] = 0

A = [i for i in xrange(-999, 1000)]
B = []
for p in primes:
    if p < 1000:
        B.append(p)
    else:
        break

remain = [[1 for j in xrange(len(B))] for i in xrange(len(A))]
num_remain = len(A)*len(B)
n = 1

while num_remain > 1:
    print n
    for i in xrange(len(remain)):
        for j in xrange(len(remain[i])):
            if remain[i][j]:
                if not(binsearch((n*n + A[i]*n + B[j]), primes, 0, len(primes))):
                    num_remain -= 1
                    remain[i][j] = 0

    n += 1
print

for i in xrange(len(remain)):
    for j in xrange(len(remain[i])):
        if remain[i][j]:
            print i, j
            print A[i], B[j], A[i]*B[j]
