T = 10
for case in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_t = list(zip(*arr)) # 배열을 돌려주자
    result = 0
    for i in arr_t: # 돌린 배열에서
        pole = 0
        for n in i:
            if n != 0 : # S극과 N극에 대해
                if n == 2 and pole == 1: #S극과 N극이 만나면
                    result += 1 #교착 +1
                pole = n #이때 n을 극값으로 저장
    print(f'#{case} {result}')