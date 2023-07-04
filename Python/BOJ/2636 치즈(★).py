def find():
    queue = deque([(0,0)])
    melt = []
    while queue:
        y, x = queue.popleft()
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                visited[ny][nx] = 1
                if cheeze[ny][nx] == 0:
                    queue.append((ny,nx))
                else :
                    melt.append((ny,nx))
    for y, x in melt:
        cheeze[y][x] = 0
    return len(melt)

import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
cheeze = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
move = [[0,1],[0,-1],[1,0],[-1,0]]
cnt = sum(sum(i) for i in cheeze)
result = 1

while True: # 반복하며 녹여보자
    visited = [[0] *M for _ in range(N)]
    now = find() 
    cnt -= now
    if cnt == 0 : # 0이 되면, now는 직전의 값
        print(result)
        print(now)
        break
    result += 1