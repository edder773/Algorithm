import sys
N = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
y = x[:]
for i in range(1, N):
    for j in range(i):
        if x[j] < x[i]:
            y[i] = max(y[i], y[j]+x[i])
print(max(y))