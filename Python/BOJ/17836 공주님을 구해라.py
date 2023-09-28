def find(a, b, cnt,  my, mx):
    queue = deque([[a, b, cnt]])
    visited = [[0] * M for _ in range(N)]
    while queue:
        y, x, cnt = queue.popleft()
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and maze[ny][nx] != 1 and not visited[ny][nx]:
                if ny == my and nx == mx:
                    return cnt + 1
                visited[ny][nx] = 1
                queue.append([ny,nx, cnt+1])
    return float('inf')

import sys
from collections import deque
N, M, T = map(int,sys.stdin.readline().split())
move = [[0,1],[0,-1],[1,0],[-1,0]]
maze = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

body = find(0, 0, 0, N-1, M-1)
for i in range(N):
    for j in range(M):
        if maze[i][j] == 2:
            temp = find(0, 0, 0, i, j)
            if temp == float('inf'):
                knife = float('inf')
            else : 
                knife = temp + abs(N-1 - i) + abs(M-1 - j)
            result = min(knife, body)
            break

if result <= T:
    print(result)
else:
    print('Fail')