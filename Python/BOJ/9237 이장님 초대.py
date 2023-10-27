import sys
N = int(sys.stdin.readline())
tree = sorted(list(map(int, sys.stdin.readline().split())),reverse=True)
result = 0
for i in range(N):
    result = max(result,tree[i] + i + 1)

print(result+1)