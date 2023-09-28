def find(a,b):
    queue = deque([[a,b]])
    visited[a][b] = 0
    while queue:
        y, x = queue.popleft()
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == -1 and land[ny][nx] == 1:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny,nx))

import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
land = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
move = [[0,1],[-1,0],[1,0],[0,-1]]

ay, ax = 0, 0

for i in range(n):
    for j in range(m):
        if land[i][j] == 2:
            ay, ax = i, j
        elif land[i][j] == 0:
            visited[i][j] = 0

find(ay,ax)
for i in visited:
    print(*i)