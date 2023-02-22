T = int(input())
for case in range(1,T+1):
    N, M = map(int, input().split())
    x = list(map(int, input().split()))
    for _ in range(M):
        y = x.pop(0)
        x.append(y)
    print(f'#{case} {x[0]}')