import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    rank = sorted([list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)])
    cnt = 1
    second_rank = rank[0][1]
    for i in range(1,N):
        if rank[i][1] < second_rank:
            cnt += 1
            second_rank = rank[i][1]
    print(cnt)