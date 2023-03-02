import sys
n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

for i in range(1,n) :
    x[i] = max(x[i], x[i-1] + x[i])
print(max(x))