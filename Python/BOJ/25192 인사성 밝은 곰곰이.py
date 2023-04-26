import sys
N = int(sys.stdin.readline())
hi = set()
result = 0
for _ in range(N):
    S = sys.stdin.readline().strip()
    if S == 'ENTER':
        result += len(hi)
        hi = set()
    else:
        hi.add(S)
result += len(hi)
print(result)