def bfs(a,b):
    move = [[1,0], [-1,0], [0,1], [0,-1]]
    queue = []
    queue.append([a,b])
    visited[a][b] = 0
    while queue:
        y, x = queue.pop(0)
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                sums = visited[y][x] + maps[ny][nx]
                if visited[ny][nx] > sums:
                    visited[ny][nx] = sums
                    queue.append([ny, nx])

T = int(input())
for case in range(1,T+1):
    N = int(input())
    maps = [list(map(int, input())) for _ in range(N)]
    visited = [[float('inf')] * N for _ in range(N)]
    bfs(0,0)
    print(f'#{case} {visited[N-1][N-1]}')