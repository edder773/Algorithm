def ripe(): # 3차원 리스트의 BFS
    while queue:
        z, y, x = queue.popleft()
        for dz, dy, dx in spread:
            nz, ny, nx = z + dz, y + dy, x + dx
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and tomato[nz][ny][nx] == 0:
                tomato[nz][ny][nx] = tomato[z][y][x] + 1
                queue.append([nz, ny, nx])

import sys
from collections import deque
M, N, H = map(int, sys.stdin.readline().split())
tomato =[[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
spread = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
queue = deque()
num = out = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                queue.append([i,j,k]) # 시작 지점을 queue에 삽입
ripe()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 0: #만약 0인게 남아있으면
                out = 1 # out에 1저장
            if num < tomato[i][j][k]: #3차원 배열의 최대값 구하기
                num = tomato[i][j][k]
if out == 0 :
    print(num-1)
else :
    print(-1)
