T = int(input())
for case in range(1, T+1):
    N = int(input())
    x = [list(map(int, input().split())) for i in range(N)]

    print(f'#{case}')
    for i in range(N):
        temp90 = []
        temp180 = []
        temp270 = []
        for j in range(N):
            temp90 += [x[N-j-1][i]]  # 90도 돌린 행렬
            temp180 += [x[N-i-1][N-j-1]]  # 180도 돌린 행렬
            temp270 += [x[j][N - i - 1]]  # 270도 돌린 행렬
        print(*temp90, ' ', *temp180, ' ', *temp270, sep='')
