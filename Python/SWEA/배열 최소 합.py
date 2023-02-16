# T = int(input())
# def back(n,min_n):
#     global m
#     if min_n > m : #애초부터 크면
#         return #끝내버리기
#     if n == N: # 전부 True일때의
#         if min_n < m :
#             m = min_n #최소값
#         return
#     for i in range(N): #한정조건 (같은 열 선택 불가 조건)
#         if check[i] == False:
#             check[i] = True
#             back(n+1,min_n+x[n][i])
#             check[i] = False
#     return
#
# for case in range(1,T+1):
#     N = int(input())
#     m = 10 * N
#     x = [0]*N
#     check = [False]*N
#     for w in range(N):
#         x[w] = list(map(int, input().split()))
#     back(0,0)
#     print(f'#{case} {m}')

def f(i, k):
    global minV
    if i == k : # 순열 완성
        s = 0
        for j in range(N):
            s += arr[j][p[j]]  # j 행에서 고른 열 p[j]
        if minV > s:
            minV = s
        return
    else :
        for j in range(i, N) : #p[i]의 숫자를 자신부터 오른쪽과 교환
            p[i], p[j] = p[j], p[i]
            f(i+1, k)
            p[i], p[j] = p[j], p[i]
    return
T = int(input())
for case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [i for i in range(N)] # p[i] i행에서 선택한 열
    minV = 10*N # 자연수
    f(0,N)
    print(f'#{case} {minV}')