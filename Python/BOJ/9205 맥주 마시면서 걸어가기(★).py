def find():
    queue = deque([[homey, homex]])
    while queue:
        y, x = queue.popleft()
        if abs(y-festy) + abs(x-festx) <= 1000: # 축제장에 도착할 수 있으면
            return "happy" # 성공
        for i in range(n):
            if not visited[i]:
                ny, nx = Songdo[i]
                if abs(y - ny) + abs(x - nx) <= 1000: # 다음 편의점까지 1000m 이하면
                    visited[i] = 1 # 방문하고
                    queue.append([ny,nx]) # 다시 출발
    return "sad" # 다 돌았음에도 반환 못하므로 sad

import sys
from collections import deque
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    homey, homex = map(int, sys.stdin.readline().split())
    Songdo = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    festy, festx = map(int, sys.stdin.readline().split())
    visited = [0]*(n+1)
    print(find())