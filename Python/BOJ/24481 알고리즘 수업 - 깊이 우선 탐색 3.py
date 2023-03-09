import sys
sys.setrecursionlimit(200000)

def dfs(n, depth):
    visited[n] = depth
    graph[n].sort()
    for i in graph[n]:
        if visited[i] == -1:
            dfs(i,depth+1)

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [-1]*(N+1)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
dfs(R,0)

for i in range(1,N+1):
    print(visited[i])