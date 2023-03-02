T = int(input())
for case in range(1, T+1):
    N = int(input())
    x = list(map(int, input().split()))

    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    print(f"#{case} ", end='')
    print(*x)
