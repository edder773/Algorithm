def bfs(a,b,K):
    visited[a][b] = 1
    queue = deque()
    queue.append([a,b])
    while queue:
        y, x = queue.popleft()
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0 and safety[ny][nx] > K :
                visited[ny][nx] = 1
                queue.append([ny,nx])

import sys
from collections import deque
N = int(sys.stdin.readline())
safety = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
move = [[1,0],[-1,0],[0,1],[0,-1]]
result = 0
for k in range(max(map(max, safety))):
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if safety[i][j] > k and visited[i][j] == 0:
                bfs(i,j,k)
                cnt += 1
    result = max(result, cnt)
print(result)