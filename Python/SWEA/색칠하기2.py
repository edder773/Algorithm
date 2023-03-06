T = int(input())
for case in range(1,T+1):
    N = int(input())
    board = [[0]*12 for _ in range(12)] # 밖으로 나가는 범위까지 고려
    move = [[1, 0],[-1, 0],[0, 1],[0, -1]]
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1+1,r2+2):
            for j in range(c1+1,c2+2):
                if color == 1:
                    board[i][j] += 1
                elif color == 2:
                    board[i][j] -= 1
    # 위까지 입력조건

    cnt = 0
    for i in range(1,12):
        for j in range(1,12):
            if board[i][j] == 1 or board[i][j] == -1: #만약 파란색이나 빨간색이면
                for dy, dx in move: # 한 칸의 4방향에 대해
                    y, x = i + dy, j + dx
                    if board[y][x] != board[i][j]: # 연결된 칸이 아니면
                        cnt += 1 # 둘레 1증가
    print(f'#{case} {cnt}')