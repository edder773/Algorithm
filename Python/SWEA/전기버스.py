T = int(input())
for case in range(1, T+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    station = [0 for _ in range(N+1)]
    for i in charge:
        station[i] += 1
    location = 0
    position = 0
    cnt = 0
    location += K
    while True:
        if location >= N:
            break
        if station[location] == 1:
            cnt += 1
            position = location
            location += K
        else:
            location -= 1
            if position == location:
                cnt = 0
                break
    print(f'#{case} {cnt}')
