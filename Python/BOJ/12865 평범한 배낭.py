# import sys
# N, K = map(int, sys.stdin.readline().split())
# items = [[0,0]]+[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# dp = [[0]*(K+1) for _ in range(N+1)]
# for i in range(1, N+1):
#     for j in range(1, K+1):
#         if j < items[i][0]: # 아이템 무게보다 더 나가면
#             dp[i][j] = dp[i-1][j] # 이전 값
#         else : # 아니면
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j - items[i][0]]+items[i][1]) # 이전 가치 / 현재가치 + 합할 수 있는 가치 합 비교
# print(dp[N][K])

import sys
N, K = map(int, sys.stdin.readline().split())
bag = {0 : 0}
for _ in range(N):
    weight, value = map(int, sys.stdin.readline().split())
    temp = {}
    for i, j in bag.items():
        w, v = weight + j, value + i
        if w < bag.get(v, K+1):
            temp[v] = w
    bag.update(temp)
print(max(bag.keys()))