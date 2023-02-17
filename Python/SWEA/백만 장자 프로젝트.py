T = int(input())
for case in range(1, T+1):
    N = int(input())
    x = list(map(int, input().split()))

    i = result = 0
    while i < N:
        i_max = i
        for j in range(i+1, N):
            if x[i_max] < x[j]:
                i_max = j

        for k in range(i, i_max):
            result += x[i_max]-x[k]
        i = i_max + 1

    print(f'#{case} {result}')

# T = int(input())
# for case in range(1, T + 1):
#     N = int(input())
#     x = list(map(int, input().split()))[::-1]
#
#     result = mx = 0
#     for n in x: # x의 요소에 대해
#         if mx > n: # mx보다 크면
#             result += mx-n #result에 최대와 n의 차만큼 저장
#         else:
#             mx = n
#
#     print(f'#{case} {result}')