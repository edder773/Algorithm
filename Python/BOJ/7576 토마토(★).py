def ripe():
    while queue:
        y, x = queue.popleft()
        for dy, dx in spread:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and tomato[ny][nx] == 0:
                tomato[ny][nx] = tomato[y][x] + 1
                queue.append([ny, nx])

import sys
from collections import deque
M, N = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
spread = [[1,0],[-1,0],[0,1],[0,-1]] # 이동 값
queue = deque()
out = 0

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i,j])

ripe() # 탐색을 돌리자

for i in tomato: 
    for j in i: #전체 토마토에 대해
        if j == 0: # 돌렸는데 0이 남아있으면
            out = 1 # 1 저장

if out == 0: # 전부 익었다면
    print(max(map(max,tomato))-1) # 토마토 내에서 제일 큰값 -1
elif out == 1: # 안익는 부분 있다면
    print(-1) # -1 출력