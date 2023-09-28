def find(c,r,d,now,result):
    if c == N-1:
        return min(now, result)
    for i in move:
        if i != d and 0 <= c < N and 0 <= r+i < M:
            now = find(c+1, r+i, i, now, result + fuel[c+1][r+i])
    return now

import sys
sys.setrecursionlimit(100000)
N, M = map(int, sys.stdin.readline().split())
fuel = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
move = [-1, 0, 1]
result = int(10e9)
for i in range(M):
    result = find(0, i, 2, result, fuel[0][i])
print(result)