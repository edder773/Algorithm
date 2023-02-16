T = int(input())
for case in range(1, T+1):
    N = int(input())
    x = [list(input().split()) for _ in range(N)]
    temp = []
    for i in range(N):
        temp += [x[i][0]]*int(x[i][1])  # temp에 모든 요소 갯수 넣기
    print(f'#{case}')
    for i in range(len(temp)//10+1):  # 전체 갯수/10 +1개 동안
        print(''.join(temp[i*(10):(i+1)*(10)]))  # 10개씩 자른거 출력
