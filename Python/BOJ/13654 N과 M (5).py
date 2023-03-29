def backtracking():
    if len(S) == M:
        print(*S)
        return
    for i in range(1,N+1):
        if x[i-1] not in S:
            S.append(x[i-1])
            backtracking()
            S.pop()

import sys
N, M = map(int, sys.stdin.readline().split())
x = sorted(list(map(int,sys.stdin.readline().split())))
S = []
backtracking()
