def prime(n):
    arr = [True] * n
    m = int(n**0.5)
    for i in range(2, m + 1):
        if arr[i] == True:
            for j in range(i * i, n, i):
                arr[j] = False
    return [i for i in range(2, n) if arr[i] == True]


primes = prime(1500000)
import sys
N = int(sys.stdin.readline())
for x in primes :
    if x >= N and str(x) == str(x)[::-1]:
        print(x)
        break
