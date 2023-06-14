# 향상된 다이나믹 프로그래밍
def find(n):
    if n in dp.keys():
        return dp[n]

    if n % 3 == 0 and n % 2 == 0:
        dp[n] = min(find(n//3) +1, find(n//2) + 1)
    elif n % 3 == 0:
        dp[n] = min(find(n//3) +1, find(n-1) + 1)
    elif n % 2 == 0:
        dp[n] = min(find(n//2) +1, find(n-1) + 1)
    else : 
        dp[n] = find(n-1) + 1
    return dp[n]

import sys
X = int(sys.stdin.readline())
dp = {1:0}
print(find(X))