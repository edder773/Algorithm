import sys
n = int(sys.stdin.readline())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    num = a*b
    while b :
        mod = b
        b = a % b
        a = mod
    print(num//a)