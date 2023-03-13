import sys
sys.setrecursionlimit(200000)

def dfs(t):
    global cnt
    depth[t] = cnt
    graph[t].sort()
    for i in graph[t]:
        if visited[i] == -1:
            cnt +=1
            visited[i] = visited[t] + 1
            dfs(i)

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [-1]*(N+1)
visited[R] = 0
depth = [0]*(N+1) 
result = 0
cnt = 1

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(R)

for i in range(N+1):
    result += visited[i] * depth[i]
print(result)
