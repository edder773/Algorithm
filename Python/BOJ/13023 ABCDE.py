def dfs(start, n):
    global result
    if n == 4:
        result = True
        return 
    visited[start] = 1
    

    for i in graph[start]:
        if not visited[i]:
            dfs(i, n+1)
    visited[start] = 0


import sys
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]
visited = [0]*(N)
result = False

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    dfs(i,0)
    if result:
        print(1)
        break
else :
    print(0)