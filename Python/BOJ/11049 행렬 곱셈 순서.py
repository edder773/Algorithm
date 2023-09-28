import sys

N = int(sys.stdin.readline())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[float('inf')] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = 0

for i in range(1, N):
    for j in range(N - i):
        for k in range(j, i + j):
            a, b, c = j, k, i + j
            dp[a][c] = min(
                dp[a][c], dp[a][b] + dp[b + 1][c] + A[a][0] * A[b][1] * A[c][1]
            )
print(dp[0][N - 1])
