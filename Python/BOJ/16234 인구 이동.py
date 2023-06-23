def find(a,b):
    people = [[a,b]]
    queue = deque([[a,b]])
    visited[a][b] = 1
    while queue:
         y, x = queue.popleft()
         for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and L <= abs(border[ny][nx] - border[y][x]) <= R:
                visited[ny][nx] = 1              
                queue.append([ny,nx])
                people.append([ny,nx])
    return people

import sys
from collections import deque
N, L, R = map(int, sys.stdin.readline().split())
border = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
move = [[1,0],[-1,0],[0,1],[0,-1]]
day, check = -1, 1
while check:
    check = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
         for j in range(N):
            if not visited[i][j]:
                country = find(i,j)
                if len(country) > 1 :
                    check = 1
                    mix = sum([border[y][x] for y, x in country]) // len(country)
                    for y, x in country:
                        border[y][x] = mix
    day += 1

print(day)