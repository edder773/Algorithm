import sys
n = int(sys.stdin.readline())
x = [0]*n
x_sum = [0]*n
for w in range(n):
    x[w] = int(sys.stdin.readline())

if len(x) <= 2:
    print(sum(x))  # 길이가 2 이하일 경우 합출력

else:
    for i in range(2, n):
        x_sum[0] = x[0]  # 합 리스트의 0번 인덱스에 1번째 값
        x_sum[1] = x[0]+x[1]  # 합 리스트에 1번 인덱스에 1,2번째 값의 합
        # 3번째부터 1계단 / 2계단 오르는 것 중 최대값 반환
        x_sum[i] = max(x_sum[i-3]+x[i-1]+x[i], x_sum[i-2]+x[i])
    print(x_sum[-1])
