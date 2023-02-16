T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    x = list(map(int, input().split()))
    x_max = x[0]
    x_min = x[0]
    for i in range(1, N):
        if x_max < x[i]:
            x_max = x[i]
        if x_min > x[i]:
            x_min = x[i]
    print(f"#{testcase} {x_max-x_min}")
