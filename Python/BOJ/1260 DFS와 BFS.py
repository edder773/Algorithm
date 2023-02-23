result = []
def dfs(n):
    visited1[n] = True
    print(n, end= ' ')
    for i in graph[n]:
        if not visited1[i]:
            dfs(i)

def bfs(n):
    result = []
    visited = [False]*(N+1)
    queue = [n]
    visited[n] = True
    while queue :
        a = queue.pop(0)
        if a not in result:
            result.append(a)
        for i in graph[a]:
            if not visited[i]:
                queue.append(i)
                visited[a] = True
    return result

import sys
N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1) ]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(N+1):
    graph[i].sort()

visited1=[False]*(N+1)
dfs(V)
print()
print(*bfs(V))