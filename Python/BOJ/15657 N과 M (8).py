def backtracking(n):
    if len(S) == M:
        print(*S)
        return
    for i in range(n,N+1):
        S.append(x[i-1])
        backtracking(i)
        S.pop()

import sys
N, M = map(int, sys.stdin.readline().split())
x = sorted(list(map(int, sys.stdin.readline().split())))
S = []
backtracking(1)