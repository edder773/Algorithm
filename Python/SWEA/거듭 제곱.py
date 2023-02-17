def multi(a,b):
    if b == 1:
        return a
    else :
        return multi(a, b-1) * a
for _ in range(1,11):
    T = input()
    N, M = map(int, input().split())
    print(f'#{T} {multi(N,M)}')