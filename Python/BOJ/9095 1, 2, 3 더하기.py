import sys
T = int(sys.stdin.readline())
dp = [0] * 11
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4,11):
    dp[i] = sum(dp[i-3:i])

for _ in range(T):
    n = int(sys.stdin.readline())
    print(dp[n])