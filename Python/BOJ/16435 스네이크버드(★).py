import sys
N, L = map(int, sys.stdin.readline().split())
h = sorted(list(map(int, sys.stdin.readline().split())))
for i in h:
    if L >= i :
        L += 1
print(L)