dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
a = 0
b = 0
def finding(y,x):
    global a,b
    if maze[y][x] == '3':
        a, b = y, x
        return
    for i in range(4):
        n = y + dy[i]
        m = x + dx[i]
        if 0 < n <= 16 and 0 < m <= 16:
            if maze[n][m] == '3':
                finding(n,m)
            if maze[n][m] == '0':
                maze[n][m] = 1
                finding(n,m)
    return 0

for case in range(1,11):
    T = int(input())
    maze = [0]*16
    for w in range(16):
        maze[w] = list(input())
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                finding(i, j)
                break
    if maze[a][b] == '3':
        print(f"#{case} {1}")
    else:
        print(f"#{case} {0}")