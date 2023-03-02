T = int(input())
for case in range(1,T+1):
    N, M, K = map(int, input().split())
    x = list(map(int, input().split()))
    visit = [0]*11112 # 최대 시간
    taiyaki = 0 # 붕어빵
    trying = 'Possible'
    for i in x:
        visit[i] += 1 # 손님의 방문 시간에 += 1

    for i in range(11112): # 1초부터 11111초까지
        if i > 0 and i % M == 0: # M초 지나면
            taiyaki += K # K개 붕어빵을 굽자
        taiyaki -= visit[i] # 해당 시간에 방문하는 사람 수만큼 붕어빵 빼주자
        if taiyaki < 0: # 붕어빵이 음수면
            trying = 'Impossible' #불가능
            break
    print(f'#{case} {trying}')

