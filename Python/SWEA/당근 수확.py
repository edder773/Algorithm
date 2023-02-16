def my_sum(n):
    a = 0
    for x in range(len(n)):
        a += n[x]
    return a


T = int(input())
for case in range(1, T+1):
    N = int(input())
    temp = []
    carrot = list(map(int, input().split()))
    for i in range(N):
        temp += [abs(my_sum(carrot[:i]) - my_sum(carrot[i:]))]
    temp_min = temp[0]
    cnt = 0
    for u in range(N):
        if temp_min > temp[u]:
            temp_min = temp[u]
            cnt = u
    print(f'#{case} {cnt} {temp_min}')
