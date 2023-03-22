def bomb_position(): # 폭탄 위치 찾기
    for i in range(R):
        for j in range(C):
            if bomb[i][j] == 'O':
                temp.append([i,j])

def bomb_BBAM(): #터뜨리기
    while temp:
        y, x= temp.popleft()
        bomb[y][x] = '.'
        for dy, dx in splash:
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C:
                bomb[ny][nx] = '.'
                
def bomb_set(): #폭탄 두기
    for i in range(R):
        for j in range(C):
            if bomb[i][j] == '.':
                bomb[i][j] = 'O'
import sys
from collections import deque
R, C, N = map(int, sys.stdin.readline().split())
bomb = [list(sys.stdin.readline().strip()) for _ in range(R)]
splash = [[1,0],[-1,0],[0,1],[0,-1]]
if N%2 != 0 :
    N -= 1
    while N > 0 : # 남은 시간 동안
        temp = deque() # 초기화
        bomb_position() # 폭탄 위치 찾고
        bomb_set() # 폭탄 두고
        #짝수 초에는 모든 맵에 폭탄이 무조건 배치된 상태 (무시해도됨)
        N -= 1 # 어차피 폭탄 두고 1초 동안은 안터지니 1초 무시 
        if N == 0: #만약 시간이 N초면
            break # 끝
        bomb_BBAM() #터뜨려! 
        N -= 1 #시간 1초 지나
    for i in bomb:
        print(*i,sep='')
else :
    bomb = [['O']*C for _ in range(R)]
    for i in bomb:
        print(*i,sep='')