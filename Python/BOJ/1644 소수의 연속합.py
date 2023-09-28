def prime(n):
    arr = [True] * n
    for i in range(2, int(n**0.5) + 1):
        if arr[i] == True:
            for j in range(i*i, n, i):
                arr[j] = False
    return [i for i in range(2, n) if arr[i] == True]

import sys
N = int(sys.stdin.readline())
primes = prime(4000000)
result, x = 0, 0
left, right = 0, 0
while right <= len(primes):
    x = sum(primes[left:right])
    if x == N:
        result += 1
        left += 1 
        right -= 1
    elif x < N:
        right += 1
    else :
        left += 1
        right -= 1

print(result)
