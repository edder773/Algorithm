import sys
N, M = map(int, sys.stdin.readline().split())
S = [0]*N
check = [0]*M
for i in range(N):
    S[i] = sys.stdin.readline().strip()
for j in range(M):
    check[j] = sys.stdin.readline().strip()
cnt = 0
for value in range(M):
    if check[value] in S:
        cnt += 1
print(cnt)
