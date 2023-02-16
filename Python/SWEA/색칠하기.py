T = int(input())
for case in range(1, T+1):
    N = int(input())
    s = [[0 for _ in range(10)] for i in range(10)]
    cnt = 0
    for _ in range(N):
        r1, c1, r2, c2, c = map(int, input().split())
        for i in range(c1, c2+1):
            for j in range(r1, r2+1):
                s[i][j] += 1
                if s[i][j] == 2:
                    cnt += 1
    print(f'#{case} {cnt}')
