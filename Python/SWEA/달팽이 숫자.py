T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for case in range(1, T+1):
    N = int(input())
    n = [[0]*N for _ in range(N)]
    move = 0  # 진행방향
    i = j = 0  # 숫자를 쓸 칸의 인덱스
    for k in range(1, N*N+1):
        n[i][j] = k
        ni, nj = i+di[move], j+dj[move]
        if 0 <= ni < N and 0 <= nj < N and n[ni][nj] == 0:
            i, j = ni, nj
        else:
            move = (move + 1) % 4  # 방향전환
            i, j = i + di[move], j+dj[move]
    print(f"#{case}")
    for x in n:
        print(*x)
