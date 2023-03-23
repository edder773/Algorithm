def bfs(a,b):
    queue = deque()
    queue.append([a,b])
    visited[a][b] = 1
    while queue:
        y, x = queue.popleft()
        jump = area[y][x]
        for dy, dx in [[1,0],[0,1]]:
            ny, nx = y + dy*jump, x + dx*jump
            if ny < N and nx < N and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                queue.append([ny,nx])
    

import sys
from collections import deque
N = int(sys.stdin.readline())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
bfs(0,0)
if visited[N-1][N-1] == 1:
    print("HaruHaru")
else :
    print("Hing")