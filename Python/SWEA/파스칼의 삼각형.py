T = int(input())
for case in range(1, T+1):
    N = int(input())
    n = [0]*N
    for i in range(N):
        n[i] = [1]*(i+1)  # 1로 입력

    for i in range(2, N):  # 맨 앞부분 제외
        for j in range(1, len(n[i])):
            if j < len(n[i])-1:  # 맨 뒷부분 제외
                n[i][j] = n[i-1][j-1]+n[i-1][j]  # 가운데 부분 = 이전줄 두개의 합
    print(f'#{case}')
    for i in range(N):
        print(*n[i])
