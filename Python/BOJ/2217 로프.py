import sys

N = int(sys.stdin.readline())
lope = sorted([int(sys.stdin.readline()) for _ in range(N)], reverse=True)

result = 0
for i in range(N):
    result = max(result, lope[i] * (i + 1))
print(result)
