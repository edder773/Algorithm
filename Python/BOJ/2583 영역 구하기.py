def find(a,b):
    queue = deque([[a, b]])
    visited[a][b] = 1
    m = 1
    while queue:
        y, x = queue.popleft()
        board[y][x] = 1
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < M and 0 <= nx < N and not visited[ny][nx] and board[ny][nx] == 0:
                visited[ny][nx] = 1
                board[ny][nx] = 1
                m += 1
                queue.append([ny,nx])
    return m
        

import sys
from collections import deque
M, N, K = map(int, sys.stdin.readline().split())
board = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]
move = [[0,1],[0,-1],[1,0],[-1,0]]
for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[j][i] = 1

result = []
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            result.append(find(i,j))

print(len(result))
print(*sorted(result))