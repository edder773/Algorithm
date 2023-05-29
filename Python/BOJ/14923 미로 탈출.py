def find(a,b):
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    queue = deque([[a, b, 1]])
    visited[a][b][1] = 1
    while queue:
        y, x, wall = queue.popleft()
        if y == Ey-1 and x == Ex-1:
            return visited[y][x][wall]-1
        
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if maze[ny][nx] == 0 and visited[ny][nx][wall] == 0:
                    visited[ny][nx][wall] = visited[y][x][wall] + 1
                    queue.append([ny,nx,wall])

                if maze[ny][nx] == 1 and wall == 1 :
                    visited[ny][nx][wall-1] = visited[y][x][wall] + 1
                    queue.append([ny,nx,wall-1])
    return -1


import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
Hy, Hx = map(int, sys.stdin.readline().split())
Ey, Ex = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
move = [[-1,0],[1,0],[0,1],[0,-1]]
print(find(Hy-1,Hx-1))