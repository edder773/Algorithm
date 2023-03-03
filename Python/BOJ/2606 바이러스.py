def dfs(n):
    visited = [False for _ in range(Com+1)]
    queue = [n]
    visited[n] = True
    result = []
    while queue:
        a = queue.pop(0)
        if a != 1 :
            result.append(a)
        for i in graph[a]:
            if not visited[i]:
                queue.append(i)
                visited[a] = True
    return len(set(result))

import sys
Com = int(sys.stdin.readline())
C = int(sys.stdin.readline())
graph = [[] for _ in range(Com+1)]
for i in range(C):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
print(dfs(1))