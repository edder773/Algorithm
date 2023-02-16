for case in range(1, 11):
    T = int(input())
    m = [list(map(int, input().split())) for _ in range(100)]
    dx = [0, 1, -1]  # 아래 / 오른쪽 / 왼쪽
    dy = [1, 0, 0]
    result = 0
    for i in range(100):
        if m[0][i]:
            y, x = 0, i
            move = 0
            while y < 99:
                if move == 0:
                    if x < 99 and m[y][x+1] == 1:
                        move = 1
                    elif x > 0 and m[y][x-1] == 1:
                        move = 2
                else:
                    if m[y+1][x]:
                        move = 0
                x += dx[move]
                y += dy[move]

            if m[y][x] == 2:
                result = i
                break
    print(f'#{case} {result}')
