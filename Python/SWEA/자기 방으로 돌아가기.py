T = int(input())
for case in range(1, T+1):
    N = int(input())
    room = [0 for _ in range(401)]
    for i in range(N):
        start, end = map(int, input().split())
        for i in range(min((start+1)//2, (end+1)//2), max((start+1)//2, (end+1)//2)+1):
            room[i] += 1
    print(f'#{case} {max(room)}')
