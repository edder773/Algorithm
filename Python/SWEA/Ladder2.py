for case in range(1, 11):
    T = int(input())
    # 2로만 구성된 100번째 행 추가
    m = [list(map(int, input().split()))
         for _ in range(100)] + [[2 for i in range(100)]]

    dx = [0, 1, -1]  # 아래 / 오른쪽 / 왼쪽
    dy = [1, 0, 0]
    result = 0
    cnt = 0
    cnt_min = 5000  # 최소 이동 횟수 측정
    for i in range(100):
        if m[0][i]:
            y, x = 0, i
            move = 0
            while y < 100:  # 100번째 행에 도착할때까지 움직인 횟수 측정(cnt)
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
                cnt += 1

            if m[y][x] == 2:  # 100번째 행에 도착했을 때
                if cnt < cnt_min:  # cnt 최솟값 측정
                    cnt_min = cnt
                    result = i  # 최소일 때의 i값(사다리번호) 저장
                cnt = 0
    print(f'#{case} {result}')
