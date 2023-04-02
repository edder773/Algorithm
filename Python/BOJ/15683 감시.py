# 조건 1 : CCTV는 감시할 수 있는 방향에 있는 칸 전체 감시 가능
# 조건 2 : CCTV는 벽을 통과할 수 없음
# 조건 3 : CCTV는 90도 방향으로 회전 가능
# 조건 4 : CCTV끼리는 통과 가능!
# 조건 5 : 사각지대 최소 크기는?

import sys, copy
N, M = map(int, sys.stdin.readline().split())
office = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
watch = [[], [[0],[1],[2],[3]], [[0,2],[1,3]], [[0,1], [1,2], [2,3], [0,3]], [[0,1,2],[0,1,3],[0,2,3],[1,2,3]], [[0,1,2,3]]]
dy = [-1,0,1,0]
dx = [0,1,0,-1]

result = float('inf')
position = []
for i in range(N): # CCTV 위치
    for j in range(M):
        if office[i][j] != 0 and office[i][j] != 6:
            position.append([i,j, office[i][j]])

def watcing(offices,watches,x,y): # CCTV 볼 수 있는 곳 체크
    for i in watches: # 감시 방향에 대해
        ny, nx = y, x
        while True:
            ny += dy[i]
            nx += dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if offices[ny][nx] == 0: # 가능하면
                    offices[ny][nx] = '#' # 표시
                elif offices[ny][nx] == 6: # 벽만나면
                    break #끝
            else : # 벗어나도 끝
                break
            
def finding(x,offices):
    global result
    if x == len(position): # 다 찾아봤으면
        sums = 0
        for i in range(N):
            for j in range(M):
                if offices[i][j] == 0: 
                    sums += 1 # 0 갯수 세기
        result = min(result, sums)
        return
    temp = copy.deepcopy(offices) # 사무실 복사
    a, b, c = position[x] 
    for i in watch[c]: # 다 뒤져보자
        watcing(temp,i,b,a) # CCTV 체크
        finding(x+1,temp) # 전부 반복
        temp = copy.deepcopy(offices)
finding(0,office)
print(result)