import sys
T = int(sys.stdin.readline())
dp = [1] * 10001 # 1이 추가되는 경우
for i in range(2, 10001): # 2가 추가되는 경우
    dp[i] += dp[i-2] 
for i in range(3, 10001): #3이 추가되는 경우
    dp[i] += dp[i-3]
for _ in range(T):
    n = int(sys.stdin.readline())
    print(dp[n])