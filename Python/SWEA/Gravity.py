T = int(input())
for test in range(1, T+1):
    N = int(input())
    x = list(map(int, input().split()))
    x_max = 0  # 최대값 비교

    for i in range(N):
        cnt = 0  # 낙차 수
        for j in range(i+1, N):  # 시작지점에서부터 끝까지
            if x[i] > x[j]:  # 뒤쪽에 앞에꺼보다 큰 갯수만큼
                cnt += 1  # 낙차수 +
        if cnt > x_max:  # 낙차 수 중 최대값
            x_max = cnt
    print(f'#{test} {x_max}')
