def backtracking(a,b):
    global result
    if a == N: # 수열 다 뒤졌으면
        return # 끝
    b += x[a] # 현재 인덱스 까지 합
    if b == K: # 합이 K면
        result +=1 # 횟수 +=1 하고
    backtracking(a+1,b) #인덱스 1개씨 늘려서 찾아보기
    backtracking(a+1,b-x[a])

T = int(input())
for case in range(1,T+1):
    N, K = map(int, input().split())
    x = list(map(int,input().split()))
    result = 0
    backtracking(0,0)
    print(f'#{case} {result}')