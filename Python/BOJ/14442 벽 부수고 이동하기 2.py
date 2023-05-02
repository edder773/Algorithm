def path_finding():
    visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)] # 3차원 리스트, 벽 깰 때와 안 꺨 때
    visited[0][0][K] = 1 # 초기 값은 벽을 깨지 않았으니까 1
    while queue:
        y, x, z = queue.popleft()
        if y == N-1 and x == M-1 :
            return visited[y][x][z]
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if maze[ny][nx] == 1 and z != 0 and visited[ny][nx][z-1] == 0 : #만약 벽에 만났는데 벽을 아직 안깨봤다면
                    visited[ny][nx][z-1] = visited[y][x][z] + 1 #벽을 깨고 이동해보고 거리 +1
                    queue.append([ny,nx,z-1])

                elif maze[ny][nx] == 0 and visited[ny][nx][z] == 0: # 이동할 수 있고, 아직 방문하지 않았으면
                    visited[ny][nx][z] = visited[y][x][z] + 1 # 이동하고 거리 +1
                    queue.append([ny,nx,z])
    return -1

import sys
from collections import deque
N, M, K = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
move = [[1,0], [-1,0], [0,1], [0,-1]]
queue = deque([[0,0,K]])
print(path_finding())