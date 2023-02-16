T = int(input())
for case in range(1, T+1):
    D, A, B, F = map(int, input().split())
    print(f'#{case} {(D/(A+B))*F}')
