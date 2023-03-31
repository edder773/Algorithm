def check(card,win): # 베이비 진 체크
    cnt = 0
    for num in card:
        if num: # 만약 카운팅 배열에 숫자가 들어있으면
            cnt += 1 # 횟수 증가
        else: # 없으면
            cnt = 0 # 초기화
        if cnt == 3 or num == 3: # 연속된 숫가거나 같은 숫자 3개면
            return win # 이겼다
    return 0

T = int(input())
for case in range(1,T+1):
    num = list(map(int, input().split()))
    result = 0 # 결과
    p1, p2 =[0]*10, [0]*10 # 카운팅 배열
    for i, x in enumerate(num): #카드 배치하자
        if i % 2: # 홀수면
            p2[x] += 1 # 2번 플레이어에게
            result = check(p2,2)
        else: # 짝수면
            p1[x] += 1 # 1번 플레이어에게
            result = check(p1,1)
        if result: #결과 났으면
            break # 끝
    print(f'#{case} {result}')
