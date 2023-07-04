def find():
    while Fqueue:
        y, x = Fqueue.popleft()
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and not Fvisited[ny][nx] and building[ny][nx] != '#':
                Fvisited[ny][nx] = Fvisited[y][x] + 1
                Fqueue.append((ny,nx))

    while Squeue:
        y, x = Squeue.popleft()
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w :
                if not Svisited[ny][nx] and building[ny][nx] != '#':
                    if not Fvisited[ny][nx] or Fvisited[ny][nx] > Svisited[y][x] + 1:
                        Svisited[ny][nx] = Svisited[y][x] + 1
                        Squeue.append((ny,nx))
            else :
                return Svisited[y][x]
            
    return 'IMPOSSIBLE'
    
import sys
from collections import deque
T = int(sys.stdin.readline())
for _ in range(T):
    w, h = map(int, sys.stdin.readline().split())
    building = [list(sys.stdin.readline().strip()) for _ in range(h)]
    Fvisited, Fqueue = [[0]*w for _ in range(h)], deque()
    Svisited, Squeue = [[0]*w for _ in range(h)], deque()
    move = [[0,1],[0,-1],[1,0],[-1,0]]
    for i in range(h):
        for j in range(w):
            if building[i][j] == '*':
                Fqueue.append((i,j))
                Fvisited[i][j] = 1
            elif building[i][j] == '@':
                Squeue.append((i,j))
                Svisited[i][j] = 1
    print(find())