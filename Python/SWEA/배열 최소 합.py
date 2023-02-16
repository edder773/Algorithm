T = int(input())
def back(n,min_n):
    global m
    if n == N: # 전부 True일때의
        if min_n < m :
            m = min_n #최소값
        return
    for i in range(N): #한정조건 (같은 열 선택 불가 조건)
        if check[i] == False:
            check[i] = True
            back(n+1,min_n+x[n][i])
            check[i] = False
    return

for case in range(1,T+1):
    m = 5000000
    N = int(input())
    x = [0]*N
    check = [False]*N
    for w in range(N):
        x[w] = list(map(int, input().split()))
    back(0,0)
    print(f'#{case} {m}')