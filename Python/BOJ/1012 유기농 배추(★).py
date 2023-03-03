def warm(a,b):
    visited = [[0]*M for _ in range(N)]
    queue = [[a,b]]
    visited[a][b] = 1
    cnt = 0
    while queue:
        cnt += 1
        y, x = queue.pop(0)
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0 and cabbage[ny][nx] != 0:
                visited[ny][nx] = visited[y][x] + 1
                cabbage[ny][nx] = 0 #이후 이어있는 배추 수 안세기 위해 없애주자
                queue.append([ny,nx])
    return cnt


import sys
T = int(sys.stdin.readline())
for case in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    cabbage = [[0]*M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        cabbage[b][a] = 1
    move = [[1,0],[-1,0],[0,1],[0,-1]]
    result = [] # 벌레 마리 수
    for i in range(N):
        for j in range(M):
            if cabbage[i][j] == 1:
                result.append(warm(i,j)) # 해당 지역수를 result에 추가
    print(len(result))