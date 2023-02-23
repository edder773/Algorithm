def walls(n, m): # 벽 3개 골라보자
    global clean
    if m == 3: # 벽 3개 골랐으면
        maps_c = copy.deepcopy(maps) #벽 3개 칠한걸 임시로 복사하자
        for r,c in virus(): #바이러스에 대해
            finding(r,c,maps_c) #바이러스를 퍼뜨려보자
        cleans = sum(i.count(0) for i in maps_c) # 복사한 지도에서 0의 갯수를 세보자
        clean = max(clean,cleans) # 기존 값과 새로운 값중 큰거 저장해
        return True
    
    else : # 벽 3개 고르기
        for i in range(n, N*M): #전체 범위에서
            r = i//M 
            c = i% M
            if maps[r][c] == 0: # 빈공간 일 때
                maps[r][c] = 1 # 벽 세우기
                walls(i, m+1)
                maps[r][c] = 0

def finding(a,b, maps_c): #바이러스 퍼짐을 구현하기 위한 BFS
    move = [[1,0], [-1,0], [0,1], [0,-1]] #바이러스 퍼지는 움직임
    queue = [[a,b]]
    while queue:
        y, x = queue.pop(0)
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and maps_c[ny][nx] == 0:
                maps_c[ny][nx] = 2
                queue.append([ny,nx])

def virus(): # 시작 바이러스 위치를 찾자
    result = []
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 2: # 2인 지점의 값을 저장
                result.append([i,j])
    return result

clean = 0

import sys
import copy
N, M = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
walls(0,0)
print(clean)