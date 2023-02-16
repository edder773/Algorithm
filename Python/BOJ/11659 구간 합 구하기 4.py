import sys
N, M = map(int, sys.stdin.readline().split())
x = [0]+list(map(int, sys.stdin.readline().split()))

for j in range(1, N+1):
    x[j] += x[j-1]

print(x)

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(x[b]-x[a-1])
