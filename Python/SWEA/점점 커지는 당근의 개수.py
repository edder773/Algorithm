T = int(input())
for case in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    cnt = 1
    temp = []
    for i in range(N-1):
        if C[i] < C[i+1]:
            cnt += 1
            temp += [cnt]
        if C[i] > C[i+1]:
            cnt = 1
            temp += [cnt]
    max_x = temp[0]
    for j in range(N-1):
        if max_x < temp[j]:
            max_x = temp[j]
    print(f'#{case} {max_x}')
