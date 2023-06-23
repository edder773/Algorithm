def find():
    while queue_F:
        y, x = queue_F.popleft()
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C and not visited_F[ny][nx] and maze[ny][nx] != '#':
                visited_F[ny][nx] = visited_F[y][x] + 1
                queue_F.append([ny,nx])
    
    while queue_J:
        y, x = queue_J.popleft()
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C :
                if not visited_J[ny][nx] and maze[ny][nx] != '#':
                    if not visited_F[ny][nx] or visited_F[ny][nx] > visited_J[y][x] + 1:
                        visited_J[ny][nx] = visited_J[y][x] + 1
                        queue_J.append([ny,nx])
            else : 
                return visited_J[y][x]
            
    return 'IMPOSSIBLE'

import sys
from collections import deque
R, C = map(int, sys.stdin.readline().split())
move = [[0,1],[0,-1],[1,0],[-1,0]]
# #벽 . 공간 J 시작위치 F 불난 공간
maze = [list(sys.stdin.readline().strip()) for _ in range(R)]
queue_F, queue_J = deque(), deque()
visited_J = [[0]*C for _ in range(R)]
visited_F = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            queue_J.append([i,j])
            visited_J[i][j] = 1
        if maze[i][j] == 'F':
            queue_F.append([i,j])
            visited_F[i][j] = 1
print(find())