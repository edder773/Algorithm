def backtracking():
    if len(S) == M:
        print(*S)
        return
    num = 0
    for i in range(N):
        if not visited[i] and num != x[i]:
            visited[i] = True
            S.append(x[i])
            num = x[i]
            backtracking()
            visited[i] = False
            S.pop()

import sys
N, M = map(int, sys.stdin.readline().split())
x = sorted(list(map(int, sys.stdin.readline().split())))
S = []
visited = [False]*N
backtracking()