def omok_check(y,x):
    a = b = c = d = 0
    for i in range(5):
        if 0 <= y-i < N and omok[y-i][x] == 'o': # 가로
            a += 1
        if 0 <= x-i < N and omok[y][x-i] == 'o': # 세로
            b += 1
        if 0 <= x + i < N and 0 <= y + i < N and omok[y + i][x + i] == 'o': # 오른쪽 아래 대각선
            c += 1
        if 0 <= x + i < N and 0 <= y - i < N and omok[y - i][x + i] == 'o': # 오른쪽 위 대각선
            d += 1
    if a == 5 or b == 5 or c == 5 or d == 5: # 오목이면
        return 1 # 1 반환

T = int(input())
for case in range(1, T+1):
    N = int(input())
    omok = [list(input()) for _ in range(N)]
    out = 0
    for i in range(N):
        for j in range(N):
            if omok_check(i,j) == 1: # 체크했는데 오목이면
                out = 1
                print(f'#{case} YES') # yes 출력하기
                break
        if out == 1: # 오목이 있으면
            break # 반복문 끝
    if out == 0: # 없으면
        print(f'#{case} NO') # No
