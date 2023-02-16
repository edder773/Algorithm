import sys
N, M = map(int, sys.stdin.readline().split())
all = {}
result = []
for i in range(N):
    x = sys.stdin.readline().strip()
    if x not in all:
        all[x] = i

for j in range(M):
    y = sys.stdin.readline().strip()
    if y in all:
        result.append(y)
result.sort()
print(len(result))
print('\n'.join(result), end='')
