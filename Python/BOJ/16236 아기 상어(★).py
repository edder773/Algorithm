# 조건 1. 아기상어의 크기는 2고, 1초마다 상하좌우로 이동
# 조건 2. 자기보다 큰 물고기가 있으면 못지나가고, 나머지는 지나갈 수 있음
# 조건 3. 자기보다 작은 물고기는 먹을 수 있고 크기가 같으면 못먹지만 지나갈 수 있음
# 조건 4: 먹을 물고기 없으면 momstercall
# 조건 5: 물고기 1마리 -> 먹으러 가자 / 여러마리 -> 가장 가까운 물고기 먹으러 가자
# 조건 6: 거리 = 이동 최소값, 여러마리면 왼쪽 친구 냠냠

def fish_yammy(a,b): # 먹으러가자 아아아
    global shark
    shark_move = [[0]*N for _ in range(N)] # 상어의 거리 체크
    shark_visit = [[0]*N for _ in range(N)] # 상어 방문 체크
    queue = deque()
    queue.append([a,b])
    shark_visit[a][b] = 1
    eat_fish = [] # 먹을 수 있는 물고기 체크
    while queue:
        y, x = queue.popleft()
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and shark_visit[ny][nx] == 0: # 방문하지 않은 곳이고
                if shark >= fish[ny][nx] : # 조건 2 : 상어가 물고기보다 크거나 같아!
                    shark_visit[ny][nx] = 1 # 방문 처리하고
                    shark_move[ny][nx] = shark_move[y][x]+1 #거리 재보자
                    queue.append([ny,nx])
                    if fish[ny][nx] and shark > fish[ny][nx] : # 조건 3 : 그 중에서 물고기가 있고, 상어가 물고기보다 커!
                        eat_fish.append([ny,nx,shark_move[ny][nx]]) # Yammy

    return sorted(eat_fish, key=lambda x : (-x[2],-x[0],-x[1])) # 조건 6 :거리, 왼쪽, 위쪽 순으로 정렬

import sys
from collections import deque

N = int(sys.stdin.readline())
fish = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
move = [[0,1],[0,-1],[1,0],[-1,0]]
y, x = 0, 0
shark, result = 2, 0 # 조건 1: 상어크기 2로 시작

for i in range(N): # 최초 상어의 위치
    for j in range(N):
        if fish[i][j] == 9 :
            y, x = i, j
            
eat_fish = 0 
while True:
    catch_fish = fish_yammy(y,x) # 조건 5 : 잡은 물고기 친구들 중에 하나씩 먹어보자
    if not catch_fish : # 잡은 물고기가 없네?
        break # 조건 4 : 엄마 소환

    cy, cx, time = catch_fish.pop() # 잡은 물고기의 위치와 걸리는 시간
    result += time # 물고기를 먹으러 가야하니까 시간(거리)만큼 증가
    fish[y][x] = fish[cy][cx] = 0 # 상어 자리, 물고기 자리 증가

    y, x = cy, cx # 물고기 먹은 자리로 상어 이동
    eat_fish += 1 # 물고기 냠냠

    if eat_fish == shark: # 자신의 크기와 같은 수의 물고기를 먹었으면
        shark += 1 # 상어 사이즈 증가
        eat_fish = 0 # 먹은 물고기 초기화

print(result)