def dfs(y,x):
    move = [[1,0], [-1,0], [0,1], [0,-1]]
    stack = []
    visited = [[False]*100 for _ in range(100)]

    stack.append([y,x])
    visited[y][x] == True
    while stack:
        y,x = stack.pop()
        for dy, dx in move:
            ny = y+dy
            nx = x+dx
            if maze[ny][nx] != 1 and not visited[ny][nx]:
                if maze[ny][nx] == 3:
                    return 1
                stack.append([ny, nx])
                visited[ny][nx] = True
    return 0
for case in range(1, 11):
    T = int(input())
    maze = [list(map(int, input())) for _ in range(100)]
    print(f'#{T} {dfs(1,1)}')
