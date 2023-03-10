def bfs(a,b):
    queue = deque()
    visited = [[0]*w for _ in range(h)]
    visited[a][b] = 1
    queue.append([a,b])
    while queue:
        y, x = queue.popleft()
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and visited[ny][nx] == 0 and maps[ny][nx] == 1:
                visited[ny][nx] = visited[y][x] + 1
                maps[ny][nx] = 0
                queue.append([ny,nx])
        

import sys
from collections import deque
move = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
while True:
    w, h = map(int, sys.stdin.readline().strip().split())
    if w == h == 0:
        break
    maps = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    result = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                bfs(i,j)
    for i in range(h):
        result += sum(maps[i])
    print(result)


