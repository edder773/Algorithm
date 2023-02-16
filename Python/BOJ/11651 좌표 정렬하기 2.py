import sys
N = int(sys.stdin.readline())
P = [0]*N
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    P[i] = (x, y)
P.sort(key=lambda c: (c[1], c[0]))
for j in range(N):
    print(*P[j])
