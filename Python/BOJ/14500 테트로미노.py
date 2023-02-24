import sys
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
move = [[1,0],[-1,0],[0,1],[0,-1]]
visited = [[False]*M for _ in range(N)]

num = 0

def dfs(i, j, d, cnt):
    global num
    if cnt == 4: # 길이가 4면
        num = max(num, d) # num에 최대값 반환
        return
    
    for y, x in move:
        dy, dx = i + y, j + x
        if 0 <= dy < N and 0 <= dx < M and not visited[dy][dx]: #방문하지 않은 범위 내에서
            visited[dy][dx] = True # 방문
            dfs(dy, dx, d + board[dy][dx], cnt+1) #횟수 1회와 방문한 칸수의 값 증가
            visited[dy][dx] = False

def fky(i,j): # ㅗ ㅜ ㅏ ㅓ를 구해주자
    global num
    for n in range(4):
        temp = board[i][j] #시작 위치의 값 저장
        for m in range(3):
            t = (n+m) % 4 # 012, 123, 230, 301 // 해당 지점기준을 기준으로 상하좌우 4영역중 3개 찍는 경우
            ny = i + move[t][0]
            nx = j + move[t][1]
            if not (0 <= ny < N and 0 <= nx < M):
                temp = 0
                break
            temp += board[ny][nx]
        num = max(num,temp)

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False
        fky(i,j)

print(num)