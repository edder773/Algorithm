def my_sum(n):
    a = 0
    for i in n:
        a += i
    return a


T = int(input())
for case in range(1, T+1):
    x = [list(map(int, input().split())) for _ in range(9)]
    y = list(zip(*x))

    for i in range(0, 6, 3):
        for j in range(0, 6, 3):
            num = 0
            for t in range(i, i+3):
                for p in range(j, j+3):
                    num += x[t][p]
    all = []
    for i in range(9):
        all += [my_sum(x[i])]
        all += [my_sum(y[i])]
    if len(set(all)) == 1:
        if list(set(all))[0] == num == 45:
            print(f'#{case} {1}')
        else:
            print(f'#{case} {0}')
    else:
        print(f'#{case} {0}')
