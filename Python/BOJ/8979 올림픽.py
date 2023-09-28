import sys
N, K = map(int, sys.stdin.readline().split())
medal = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)], key = lambda x : (x[1], x[2], x[3]), reverse=True)
n = [medal[i][0] for i in range(N)].index(K)

for i in range(N):
    if medal[n][1:] == medal[i][1:]:
        print(i+1)
        break