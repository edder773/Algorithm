import sys
n = int(sys.stdin.readline())
S = sorted(list(map(int, sys.stdin.readline().split())))

result = []
for i in range(n):
    result.append(S[i] + S[2*n-1-i])
print(min(result))