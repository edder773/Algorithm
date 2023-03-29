def backtracking(n):
    if len(S) == M:
        print(*S)
        return
    num = 0
    for i in range(n,N):
        if num != x[i]:
            S.append(x[i])
            num = x[i]
            backtracking(i)
            S.pop()

import sys
N, M = map(int, sys.stdin.readline().split())
x = sorted(list(map(int, sys.stdin.readline().split())))
S = []
backtracking(0)