T = int(input())
for case in range(1,T+1):
    N = int(input())
    n = N//10
    floor = [0] * (n + 1)
    floor[0] = 1
    floor[1] = 3
    for i in range(2, n + 1):
        # 수학 공식?
        if i % 2 == 1 :
            floor[i] += floor[i - 2] * 4 - 1
        elif i % 2 == 0:
            floor[i] += floor[i - 2] * 4 + 1
        # floor[i] = floor[i-1]+2*floor[i-2] 정답
    print(f'#{case} {floor[n-1]}')
