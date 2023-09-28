def find(y, x) :
    if y == N - 1 and x == M - 1:
        return 1
    
    if visited[y][x] != -1:
        return visited[y][x]
    visited[y][x] = 0
    
    for dy, dx in move:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and board[y][x] > board[ny][nx]:
            visited[y][x] += find(ny, nx)
    
    return visited[y][x]

import sys
sys.setrecursionlimit(100000)
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
print(find(0,0))