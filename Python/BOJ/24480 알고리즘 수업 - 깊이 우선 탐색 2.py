import sys
sys.setrecursionlimit(200000)

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0]*(N+1)
cnt = 1

def dfs(n):
    global cnt
    visited[n] = cnt
    graph[n].sort(reverse=True)
    for i in graph[n]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)
dfs(R)
for i in range(1,N+1):
    print(visited[i])