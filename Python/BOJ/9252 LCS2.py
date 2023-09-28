import sys
word1, word2 = sys.stdin.readline().strip(), sys.stdin.readline().strip()
n, m = len(word1), len(word2)
dp = [['']*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1] + word1[i-1]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else :
                dp[i][j] = dp[i][j-1]
print(len(dp[n][m]))
print(dp[n][m])