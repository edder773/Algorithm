def moving(): #나이트 이동방향 bfs
    while queue:
        y, x = queue.popleft()
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < l and 0 <= nx < l and board[ny][nx] == 0:
                board[ny][nx] = board[y][x] + 1
                queue.append([ny,nx])
    return board[ea][eb]-1 # 최종 도착 지점까지 이동 횟수 반환

import sys
from collections import deque
T = int(sys.stdin.readline())
for _ in range(T):
    l = int(sys.stdin.readline())
    board = [[0]*l for _ in range(l)]
    sa, sb = map(int, sys.stdin.readline().split()) #출발점
    board[sa][sb] = 1
    ea, eb = map(int, sys.stdin.readline().split()) #도착점
    move = [[2,-1],[2,1],[1,2],[1,-2],[-2,1],[-2,-1],[-1,2],[-1,-2]] # 나이트 이동 방향
    queue = deque()
    queue.append([sa,sb])
    print(moving())