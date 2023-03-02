import sys
N = int(sys.stdin.readline())
board = [0]*N
for new in range(N):
    board[new] = list(map(int, sys.stdin.readline().split())) #칸 만들기

cnt = 0
def searching(x,y,location): # location 기준 가로 :0 세로 : 1 대각 : 2
    global cnt
    if x == N-1 and y == N-1: # x,y 칸이 (N-1,N-1)에 도착하면 반환
        cnt += 1
        return
    if location == 0 or location == 2 : #가로나 대각으로 누워있을 때
        if y + 1 < N and board[x][y+1] == 0:  #가로로 갈 수 있다면
            searching(x,y+1,0) # 가로 증가
    if location == 1 or location == 2 : #세로나 대각으로 누워있을 떄
        if x + 1 < N and board[x+1][y] == 0: #세로로 갈 수 있다면
            searching(x+1,y,1) # 세로 증가
    if x <N-1 and y< N-1 : # 그외 가로나 세로 끝에 도착 하지 않았다면
        if board[x+1][y+1] == 0 and board[x+1][y] == 0 and board[x][y+1] == 0: #만약 가로 세로 대각이 비었다면
            searching(x+1,y+1,2) #대각선 증가

searching(0,1,0) # 시작지점 파이프 대가리 기준 0,1,0에서 시작
# 문제에 *벽*이 존재
# 벽이 그러면 도착지점에 있다면? 애초에 방법이 없으니 cnt = 0?
if board[N-1][N-1] == 1 :
    print(0)
else :
    print(cnt)