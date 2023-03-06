# T = int(input())
# for case in range(1,T+1):
#     N, M = map(int, input().split())
#     flag = [list(input()) for _ in range(N)]
#     result = float('inf')
#     for i in range(N):
#         for j in range(i+1,M):
#             w, b, r = 0, 0, 0
#             white, blue, red = flag[:i], flag[i:j], flag[j:] #흰색, 파란색, 빨간색 범위
#             if len(white) > 0 and len(blue) > 0 and len(red) > 0 :
#                 # 각 요소에 대해 전체 원소 갯수 - 영역에 해당하는 갯수 하면 칠해야할 갯수가 나온다
#                 w = len(white)*M - sum([a.count('W') for a in white]) # 흰색영역 W 갯수
#                 b = len(blue)*M - sum([bb.count('B') for bb in blue]) # 파란색영역 B 갯수
#                 r = len(red)*M - sum([c.count('R') for c in red])# 빨간색영역 R 갯수
#                 result = min(result, (w + b + r))
#     print(f'#{case} {result}')

T = int(input())
for case in range(1,T+1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    result = float('inf')
    for a in range(N-2):
        for b in range(a+1, N-1):
            cnt = 0
            for i in range(a+1):
                for j in range(M):
                    if flag[i][j] != 'W':
                        cnt += 1

            for i in range(a+1, b+1):
                for j in range(M):
                    if flag[i][j] != 'B':
                        cnt += 1

            for i in range(b+1, N):
                for j in range(M):
                    if flag[i][j] != 'R':
                        cnt += 1
            result = min(result, cnt)
    print(f'#{case} {result}')
