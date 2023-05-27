def treasure_hunt(a,b):
    visited = [[0]*M for _ in range(N)]
    visited[a][b] = 1
    queue = deque([[a,b]])
    while queue:
        y, x = queue.popleft()
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and chart[ny][nx] == 'L' and not visited[ny][nx]:
                visited[ny][nx] = visited[y][x] + 1
                queue.append([ny,nx])
    return visited[y][x]

import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
chart = [list(sys.stdin.readline().strip()) for _ in range(N)] # 지도
move = [[1,0],[-1,0],[0,1],[0,-1]]
result = 0

for i in range(N):
    for j in range(M):
        if chart[i][j] == 'L': # L이면 탐색
            result = max(result, treasure_hunt(i,j)) # 둘중 최대 값

print(result -1)