import sys
N = int(sys.stdin.readline())
income = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [0]*(N+1)
for i in range(N):
    for j in range(i+income[i][0],N+1):
        if dp[j] < dp[i]+income[i][1]:
            dp[j] = dp[i]+income[i][1]
print(dp[-1])