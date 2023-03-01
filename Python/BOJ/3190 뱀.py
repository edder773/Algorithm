# 값 받기
import sys
from collections import deque 
N = int(sys.stdin.readline())
board = [[0]*N for _ in range(N)]
K = int(sys.stdin.readline())
for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    board[a-1][b-1]= 2
L = int(sys.stdin.readline())
move = [0]*L
for j in range(L):
    move[j] = list(sys.stdin.readline().split())
dy = [0,1,0,-1]
dx = [1,0,-1,0]
go, cnt = 0, 0 # 이동 방향 / 시간
y, x = 0, 0 # 현재 뱀 머리 위치
board[y][x] = 1
snake = deque([[0,0]]) # 뱀 전체 몸

while True: # 범위내에서 도는 동안
    cnt += 1 # 시간 + 1
    y, x = y + dy[go], x + dx[go] # go에 따른 이동
    if y < 0 or y >= N or x < 0 or x >= N or [y,x] in snake : #만약 머리가 뱀 몸 안에 있으면
        break # 끝
    if board[y][x] != 2: # 사과를 먹지 않았다면
        a, b = snake.popleft() # 이동했으므로 꼬리 끝부분 이동
        board[a][b] = 0 # 꼬리 지나간 부분은 0으로 바꾸기
    board[y][x] = 1 # 뱀의 몸이 있는 부분
    snake.append([y,x]) #뱀의 머리를 추가
    
    for num, c in move : # 시간과 방향에 대해
        if cnt == int(num): # 시간이 num초 
            if c == 'D': # 흐르고 D라면
                go = (go+1)%4 # 시계방향으로 가!
            else : # 아니라면
                go = (go-1)%4 # 반시계방향으로 가!
print(cnt)