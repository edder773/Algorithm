T = int(input())
for case in range(1, T+1):
    N, M, K, H = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            near = []
            a1, a2, a3 = x[i-1][j-1], x[i-1][j], x[i-1][j+1]  # 왼쪽위 위 오른쪽위
            a4, a5, a6 = x[i][j-1], x[i][j], x[i][j+1]  # 왼쪽 착륙지점 오른쪽
            a7, a8, a9 = x[i+1][j-1], x[i+1][j], x[i+1][j+1]  # 왼쪽아래 아래 오른쪽아래
            near += [a1, a2, a3, a4, a6, a7, a8, a9]
            if max(near)-min(near) <= K and (a5 >= min(near) and (a5 - min(near) <= H)):  # 조건 1과 조건 2
                cnt += 1
    print(f'#{case} {cnt}')
