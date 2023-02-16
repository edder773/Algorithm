import sys
N = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
y = [1]*N

for i in range(1, N):
    for j in range(0, i):
        if x[j] < x[i]:
            y[i] = max(y[i], y[j]+1)

for m in range(1, N):
    for n in range(m):
        if x[n] > x[m]:
            y[m] = max(y[m], y[n]+1)

print(max(y))
