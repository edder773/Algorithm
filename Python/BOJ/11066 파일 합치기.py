import sys
T = int(sys.stdin.readline())
for _ in range(T):
    K = int(sys.stdin.readline())
    size = [0] + list(map(int, sys.stdin.readline().split()))
    sized = [0]*(K+1)
    dp = [[0]*(K+1) for _ in range(K+1)]
    for i in range(1, K+1):
        sized[i] = sized[i-1] + size[i]
    
    for i in range(2, K+1):
        for j in range(1, K+2-i):
            dp[j][j+i-1] = min([dp[j][j+k] + dp[j+k+1][j+i-1] for k in range(i-1)]) +(sized[j+i-1] - sized[j-1])
    print(dp[1][K])