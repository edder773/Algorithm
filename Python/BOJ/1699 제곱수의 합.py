import sys
N = int(sys.stdin.readline())
dp = [i for i in range(N+1)] # 0,1,2,3,4 ...
for i in range(1, N+1):
    for j in range(1, i):
        m = i - j*j # 제곱 수 체크
        if m < 0:
            break
        if dp[i] > dp[m] + 1:
            dp[i] = dp[m] + 1 #이전 제곱 수 + 1
print(dp[N])