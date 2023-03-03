from collections import deque
move = [[1,0],[-1,0],[0,1],[0,-1]]

def spin():
    queue = deque()
    for i in range(min(N,M)//2):
        r = c = i
    while True:
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if i <= nr < N - i and i <= nc < M- i:
                queue.append(arr[r][c])
                r, c = nr, nc
            else :
                break

import sys
N, M ,R = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
