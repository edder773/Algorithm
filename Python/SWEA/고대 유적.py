def check(n):
    cnt_max = 0
    for i in n:
        cnt = 0
        for j in i:
            if j == 1: # 1이면
                cnt += 1 # 갯수 증가
                if cnt_max < cnt: # 최대값 구하기
                    cnt_max = cnt
            else :
                cnt = 0
    return cnt_max # 최대값 반환


T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(N)] #가로 방향
    x_90 = list(zip(*x)) #세로 방향
    print(f'#{case} {max(check(x),check(x_90))}')