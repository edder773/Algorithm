def bfs(n):
    global cnt
    queue = [n]
    visited[n] = 1
    while queue:
        a = queue.pop(0)
        graph[a].sort(reverse=True)
        for i in graph[a]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                queue.append(i)

import sys
N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 1

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(R)
for v in visited[1:]:
    print(v)