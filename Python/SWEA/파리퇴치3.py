T = int(input())
spray_plus = [[1, 0], [-1, 0], [0, 1], [0, -1]] # + 방향
spray_X = [[1, 1], [1, -1], [-1, 1], [-1, -1]] # X 방향
for case in range(1,T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    sums_max = 0 #최대 값
    for i in range(N):
        for j in range(N):
            sums_plus = sums_X = flies[i][j] #노즐의 중심값
            for k in range(1,M):
                for dy, dx in spray_plus:
                    y, x = i + dy*k, j + dx*k # 노즐을 포함한 M 만큼의 + 방향 칸 수 고려해주자
                    if 0 <= y < N and 0 <= x < N:
                        sums_plus += flies[y][x]

            for k in range(1,M):
                for dy, dx in spray_X: # 노즐을 포함한 M 만큼의 X 방향 칸 수 고려해주자
                    y, x = i + dy * k, j + dx * k
                    if 0 <= y < N and 0 <= x < N:
                        sums_X += flies[y][x]
            sums_max = max(sums_max, sums_X, sums_plus) # X와 + 중에 제일 높은 값
    print(f'#{case} {sums_max}')