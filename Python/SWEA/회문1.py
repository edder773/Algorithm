for case in range(1, 11):
    T = int(input())
    x = [list(input()) for _ in range(8)]
    x_low = list(zip(*x))  # 열로 이루어진 행렬 생성

    cnt = 0
    for i in range(8):
        for j in range(8):
            for k in range(8):
                if j != k + 1:
                    # 가로 열에 대한 회문 찾기
                    if x[i][j:k + 1] == x[i][j:k + 1][::-1] and len(x[i][j:k+1]) == T:
                        cnt += 1
                    # 세로 열에 대한 회문 찾기
                    if x_low[i][j:k + 1] == x_low[i][j:k + 1][::-1] and len(x[i][j:k+1]) == T:
                        cnt += 1
    print(f'#{case} {cnt}')
