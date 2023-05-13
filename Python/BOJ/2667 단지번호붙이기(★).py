def complexs(a,b):
    visited = [[0]*N for _ in range(N)] # 방문 처리
    queue = [[a,b]]
    visited[a][b] = 1
    cnt = 0 # 횟수를 세어보자
    while queue:
        cnt += 1 # 갈수 있는 단지들을 세보자
        y, x = queue.pop(0)
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0 and town[ny][nx] != 0:
                visited[ny][nx] = visited[y][x] + 1 # 지나옴 체크
                town[ny][nx] = 0 # 마을 수 셋으니 이후에 안세게 건물 부숴버림
                queue.append([ny,nx])
    return cnt
        
import sys
N = int(sys.stdin.readline())
town = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
move = [[1,0],[-1,0],[0,1],[0,-1]]
result = []
for i in range(N):
    for j in range(N):
        if town[i][j] == 1: # 1로 시작하면 단지이므로
            result.append(complexs(i,j)) # 돌려서 결과에 삽입
result.sort() # 오름차순 정렬
print(len(result))
for k in range(len(result)):
    print(result[k])