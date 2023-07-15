import sys
while True:
    N, A, B= map(int, sys.stdin.readline().split())
    if N == 0 and A == 0 and B == 0 :
        break
    # A, B 까지의 거리 차이를 기준으로 큰 것부터 나오게 정렬
    teams = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)], key = lambda x : -abs(x[1] - x[2]))
    result = 0
    for K, Da, Db in teams: 
        temp = min(K, A)
        if Da >= Db : # A까지 거리가 더 길면
            temp = K - min(K, B)
        A -= temp
        B -= K - temp
        result += temp * Da + (K - temp) * Db # 거리 값 * 풍선 개수
    print(result)