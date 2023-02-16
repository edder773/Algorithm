T = int(input())
for case in range(1, T+1):
    N, K = map(int, input().split())
    x = [0]*N
    for w in range(N):
        x[w] = list(map(int, input().split()))
    y = list(zip(*x))  # 세로열
    match = 0
    # 가로열의 칸 수 찾기
    for i in range(N):
        cnt = 0
        for j in range(N):
            if x[i][j] == 1:  # 1일경우
                cnt += 1  # cnt 증가
                if j == (N-1) and cnt == K:  # 경계조건
                    match += 1
            elif x[i][j] == 0:  # 0일 경우
                if cnt == K:  # 이때의 cnt가 K랑 같으면
                    match += 1
                    cnt = 0
                else:
                    cnt = 0
    # 세로열의 칸 수 찾기
    for i in range(N):
        cnt = 0
        for j in range(N):
            if y[i][j] == 1:
                cnt += 1
                if j == (N-1) and cnt == K:
                    match += 1
            elif y[i][j] == 0:
                if cnt == K:
                    match += 1
                    cnt = 0
                else:
                    cnt = 0

    print(f'#{case} {match}')
