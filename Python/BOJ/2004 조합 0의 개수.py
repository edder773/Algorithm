import sys

def count2(n):
    if n < 2:
        return 0
    count = 0
    while n >= 2:
        count += n//2
        n = n//2
    return count

def count5(n):
    if n < 5:
        return 0
    count = 0
    while n >= 5:
        count += n//5
        n = n//5
    return count

N, M = map(int, sys.stdin.readline().split())
two = count2(N)-count2(N-M)-count2(M)
five = count5(N)-count5(N-M)-count5(M)
print(min(two, five))
