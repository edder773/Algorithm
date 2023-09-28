def find(x, cnt):
    visited[x] = 1
    for i in graph[x]:
        if not visited[i]:
            cnt = find(i, cnt+1)
    return cnt

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0]*(N+1)
    print(find(1,0))