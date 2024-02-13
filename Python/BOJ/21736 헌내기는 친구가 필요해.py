def find(a,b):
    queue = deque()
    queue.append((a,b))
    visited[a][b] = 1
    meet = 0
    while queue:
        y, x = queue.popleft()
        for dy, dx in move:
            ny, nx = dy + y, dx + x
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and not campus[ny][nx] == 'X':
                visited[ny][nx] = 1
                if campus[ny][nx] == 'P':
                    meet += 1
                queue.append((ny,nx))
    return meet

import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
campus = list(sys.stdin.readline().strip() for _ in range(N))
visited = [[0] * M for _ in range(N)]
move = [[0,1], [0,-1], [1,0], [-1,0]]
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            result = find(i,j)
            if result :
                print(result)
            else:
                print('TT')
            break