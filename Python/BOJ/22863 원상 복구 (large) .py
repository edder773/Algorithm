import sys
N, K = map(int, sys.stdin.readline().split())
P = [0] + list(map(int, input().split()))
S = [0] + list(map(int, input().split()))
D = [0]*(N+1)
result = [0]*(N+1)
visited = [False]*(N+1)
for i in range(1, N+1): 
    if visited[i]: # 찾아본거면
        continue 
    cnt, num = 0, i 
    while not visited[num]: # 방문 안했으면 // 순열 사이클 구해주는 과정
        visited[num] = True # 방문 처리하고
        D[cnt] = num # S에서 가져온 num을 D에서 추가해가기
        cnt += 1 # 인덱스 하나씩 늘려가자
        num = S[num] # S의 num 인덱스 값을 가져오기
    for j in range(cnt): # cnt = 해당 순열의 사이클 수
        x = P[D[j]] # 결과로 출력할 것의 값 = 카드 한번 바꿔 준 것 
        y = D[(j+K)%cnt] # 그때 인덱스 = j+K를 사이클로 나눠준 값
        result[y] = x # 위에 두개 반영
print(*result[1:])