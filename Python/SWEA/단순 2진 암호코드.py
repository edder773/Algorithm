T = int(input())
for case in range(1,T+1):
    N, M = map(int, input().split())
    code = [list(map(int, input())) for _ in range(N)]
    odd = 0
    even = 0
    data = [[0,0,0,1,1,0,1],[0,0,1,1,0,0,1],[0,0,1,0,0,1,1],[0,1,1,1,1,0,1],[0,1,0,0,0,1,1],[0,1,1,0,0,0,1],[0,1,0,1,1,1,1],[0,1,1,1,0,1,1],[0,1,1,0,1,1,1],[0,0,0,1,0,1,1]]
    for i in range(N): # 암호 부분 꺼내주기
        for j in range(M-1,-1,-1):
            if code[i][j] == 1:
                scan = code[i][j-55:j+1]
                break
    temp = []
    for k in range(8):
        for l in range(10):
            if scan[k*7:(k+1)*7] == data[l]: #암호랑 데이터랑 맞는 부분 숫자로 변환
                temp.append(l)
    for n in range(8):
        if n % 2 == 0 : # 짝수면
            even += temp[n]
        else : #홀수면
            odd += temp[n]
    if (even*3 + odd) % 10 == 0: # 인덱스는 0부터 시작하므로 짝수 <> 홀수 바꿔서 *3
        print(f'#{case} {odd+even}')
    else :
        print(f'#{case} {0}')
