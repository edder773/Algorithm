T = int(input())
for case in range(1,T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    cheese = []
    for i in range(M):
        cheese.append([i+1, pizza[i]]) # 치즈에 피자 인덱스랑 같이 저장
    pot = cheese[:N] # 넣은 갯수
    remains = cheese[N:] # 남은 갯수
    result = [] #결과값
    while len(pot) > 0: # 0이 될떄까지 돈다
        x = pot.pop(0) #맨 앞에꺼 꺼내서 확인
        x[1] //= 2 # 돈거기준 치즈 절반
        if x[1] == 0:
            if remains: #나머지가 있으면
                pot.append(remains.pop(0)) #나머지를 넣어줍시다
                result.append(x[0])
            else : #나머지 없으면
                result.append(x[0]) #인덱스만 받아줍시다
        else: #0 아니면
            pot.append(x) #다시 집어넣어요
    print(f'#{case} {result[-1]}')