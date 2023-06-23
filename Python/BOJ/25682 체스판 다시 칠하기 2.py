import sys
N, M, K = map(int, sys.stdin.readline().split())
chess = [list(sys.stdin.readline().strip()) for _ in range(N)]
acc = [[0] *(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if (i + j) % 2 :
            if chess[i-1][j-1] == 'W':
                acc[i][j] = acc[i-1][j] + acc[i][j-1] - acc[i-1][j-1]
            else :
                acc[i][j] = acc[i-1][j] + acc[i][j-1] - acc[i-1][j-1] + 1
        else:
            if chess[i-1][j-1] == 'B':
                acc[i][j] = acc[i-1][j] + acc[i][j-1] - acc[i-1][j-1]
            else :
                acc[i][j] = acc[i-1][j] + acc[i][j-1] - acc[i-1][j-1] + 1

result_min = float('inf')
result_max = float('-inf')

for i in range(K, N+1):
    for j in range(K, M+1):
        result_min = min(result_min, acc[i][j] - acc[i][j-K] - acc[i-K][j] + acc[i-K][j-K])
        result_max = max(result_max, acc[i][j] - acc[i][j-K] - acc[i-K][j] + acc[i-K][j-K])

print(min(result_max,result_min, K**2 - result_max, K**2 - result_min))