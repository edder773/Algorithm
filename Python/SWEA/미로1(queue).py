def bfs(a,b):
    visited = [[0]*16 for _ in range(16)]
    move = [[1,0], [-1,0], [0,1], [0,-1]] #상하좌우
    queue = []
    queue.append([a,b]) #큐에 초기값 지정
    visited[a][b] = 1 # 초기값 1
    while queue:
        y, x = queue.pop(0)
        if maze[y][x] == 3:
            return 1
        for dy, dx in move :
            ny, nx = y + dy, x + dx
            if 0 <= ny < 16 and 0 <= nx < 16 and maze[ny][nx] != 1 and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                queue.append([ny,nx])
    return 0

for case in range(1,11):
    T = int(input())
    maze = [list(map(int,input())) for _ in range(16)]
    print(f'#{case} {bfs(1,1)}')
