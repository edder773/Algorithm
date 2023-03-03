import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
ladder = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
snake = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
queue = deque()
queue.append(1)
board = [0]*101
board[1] = 1
while queue:
    a = queue.popleft()
    if a == 100:
        print(board[a]-1)
        break

    for i in [a+1,a+2,a+3,a+4,a+5,a+6]:
        if i <= 100 and board[i] == 0:
            board[i] = board[a]+1
            for k in snake:
                if i == k[0]:
                    c = i
                    i = k[1]
                    board[i] = board[c] 
            for j in ladder:
                if i == j[0]:
                    b = i
                    i = j[1]
                    board[i] = board[b]      
            queue.append(i)