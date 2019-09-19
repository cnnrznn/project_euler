N = 1000000
arr = [ 0 for i in range(N) ]

primes = []

for i in range(2, N):
    if arr[i] == 0:
        primes.append(i)
        for j in range(i, i, N):
            arr[j] = 1

print(primes)
