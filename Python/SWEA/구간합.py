def sum_list(n):
    total = 0
    for num in n:
        total += num
    return total


T = int(input())
for test in range(1, T + 1):
    N, M = map(int, input().split())
    x = list(map(int, input().split()))
    temp = [0] * N
    for i in range(N):
        temp[i] = sum_list(x[i:i + M])
    temp = temp[:(N - M + 1)]
    temp_max = temp[0]
    temp_min = temp[0]
    for j in range(len(temp)):
        if temp_max < temp[j]:
            temp_max = temp[j]
        if temp_min > temp[j]:
            temp_min = temp[j]

    print(f'#{test} {temp_max - temp_min}')
