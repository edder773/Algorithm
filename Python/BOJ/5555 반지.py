import sys
S = sys.stdin.readline().strip()
N = int(sys.stdin.readline())
result = 0
for _ in range(N):
    x = sys.stdin.readline().strip()
    if S in x*2:
        result += 1
print(result)