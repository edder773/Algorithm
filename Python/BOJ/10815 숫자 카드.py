import sys
N = int(sys.stdin.readline())
x = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
y = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    if y[i] in x:
        y[i] = 1
    else:
        y[i] = 0
print(*y)
