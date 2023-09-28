import sys
from collections import deque
N, M = map(int,sys.stdin.readline().split())
mountain = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
move = [[0,1],[0,-1],[1,0],[-1,0]]
visited = [[0]*M for _ in range(N)]
queue = deque()
for i in range(N):
    for j in range(M):
        if mountain[i][j] == 0:
            queue.append([i,j])
            visited[i][j] = 1
fire = []
while queue :
    y, x = queue.popleft()
    for dy, dx in move:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and mountain[ny][nx] == 1 and not visited[ny][nx]:
            visited[ny][nx] = visited[y][x] + 1
            queue.append([ny,nx])
            fire.append([ny,nx])

while fire:
    a, b = fire.pop()
    mountain[a][b] = 0

for i in visited:
    print(*i)