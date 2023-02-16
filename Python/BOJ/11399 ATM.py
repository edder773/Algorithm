import sys
N = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
x.sort()
for i in range(1, N):
    x[i] += x[i-1]
print(sum(x))
