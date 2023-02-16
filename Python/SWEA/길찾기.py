def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


for case in range(1, 11):
    T, N = map(int, input().split())
    x = list(map(int, input().split()))
    a = [[] for _ in range(100)]
    visited = [False] * 100
    for i in range(N):
        a[x[2*i]].append(x[(2*i)+1])
    dfs(a, 0, visited)
    if visited[99] == True:
        print(f'#{case} {1}')
    else:
        print(f'#{case} {0}')
