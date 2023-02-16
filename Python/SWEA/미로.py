T = int(input())

dx = [0, 0, 1, -1]  # 오른쪽 왼쪽
dy = [1, -1, 0, 0]  # 위 아래

a = 0
b = 0


def finding(x, y):
    global a
    global b

    if maze[y][x] == '3':
        a, b = x, y
        return

    else:
        for i in range(4):
            n = x+dx[i]  # 좌우
            m = y+dy[i]  # 상하
            if 0 <= n < N and 0 <= m < N:  # 상하좌우
                if maze[m][n] == '3':  # 3이면
                    finding(n, m)
                elif maze[m][n] == '0':  # 0일경우 > 갈 수 있으면
                    maze[m][n] = 1  # 1로 바꿈
                    finding(n, m)


for case in range(1, T+1):
    N = int(input())
    maze = [0]*N
    for t in range(N):
        maze[t] = list(input())
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                finding(j, i)

    if maze[b][a] == '3':
        print(f'#{case} 1')
    else:
        print(f'#{case} 0')
