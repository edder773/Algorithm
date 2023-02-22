# move = [[1,0], [-1,0], [0,1], [0,-1]]

# T = int(input())
# for case in range(1,T+1):
#     N, M = map(int, input().split())
#     city = [list(map(int, input().split())) for _ in range(N)]
#     serv = [k*k+(k-1)*(k-1) for k in range(N)]
#     home = []
#     for i in range(N):
#         for j in range(N):
#             if city[i][j]:
#                 home.append([i,j])
#     cnt = 0
#     for i in range(1, N+2):
#         for j in range(N):
#             for k in range(N):
#                 homes = 0
#                 for a, b in home:
#                     if abs(i-a) + abs(j-b) < k:
#                         homes += 1
#                 if homes * M - serv[k] >= 0:
#                     cnt = max(homes,cnt)
#     print(f'#{case} {cnt}')

move = [[1,0], [-1,0], [0,1], [0,-1]]
def bfs(a, b, k):
    global result
    visited = [[0]*N for _ in range(N)]
    queue = [[a,b]]
    visited[a][b] = 1
    cnt = 0
    while queue:
        y, x = queue.pop(0)
        if city[y][x] == 1:
            cnt += 1
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] ==0:
                visited[ny][nx] = visited[y][x] +1
                if visited[ny][nx] <= k: # 방문 값이 k보다 크면
                    queue.append([ny,nx])
    num = cnt * M # 면적안 집의 갯수 * 비용
    if num >= cost: #요구 비용보다 비싸면
        result = max(result, cnt)

T = int(input())
for case in range(1,T+1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for k in range(N+1, 0, -1):
        cost = k*k + (k-1)*(k-1)
        for i in range(N):
            for j in range(N):
                bfs(i,j,k)
        if result > 0:
            break
    print(f"#{case} {result}")