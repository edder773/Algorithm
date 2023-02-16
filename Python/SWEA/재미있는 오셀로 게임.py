T = int(input())
for case in range(1, T+1):
    check = [[1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]] # 8가지 방향을 고려해주자
    N, M = map(int, input().split())
    board = [[0]*(N+1) for _ in range(N+1)] # N+1칸까지 보드를 만들어줌 (입력 위치가 1부터 시작하므로)
    board[N//2][N//2] = board[N//2+1][N//2+1] = 2 # 시작 조건 백돌 2개
    board[N//2][N//2+1] = board[N//2+1][N//2] = 1 # 시작 조건 흑돌 2개
    for _ in range(M):
        a, b, color = map(int, input().split()) # 입력 조건
        board[a][b] = color # 받은 보드의 위치에 돌을 놓음
        for x, y in check: # 8방향 고려해주기
            atk = [] # 뒤집을 돌들을 저장
            for i in range(1, N):
                dx, dy = a+x*i, b+y*i #8방향의 모든 칸수 고려
                if 1 <= dx <= N and 1 <= dy <= N: #범위를 넘어서지 않는 선에서
                    if board[dx][dy] == 0: # 방향 칸에 0이라면 건들게 없음
                        break
                    elif board[dx][dy] == color: #만약 보드가 입력된 돌과 색이 같다면
                        while atk: # 뒤집을 돌이 있으면
                            a1, a2 = atk.pop() #a1,a2에 돌 위치값을 저장
                            board[a1][a2] = color #돌 위치를 돌 색과 일치 시킴
                        break
                    else: #돌 위치 색과 다르다면
                        atk.append([dx,dy]) #뒤집을 돌의 값을 입력
                else: # 범위 넘어서면 종료
                    break
    black_cnt = 0
    white_cnt = 0
    for j in board: #보드안에 있는
        black_cnt += j.count(1) # 검은 돌의 갯수
        white_cnt += j.count(2) # 흰색 돌의 갯수
    print(f"#{case} {black_cnt} {white_cnt}")