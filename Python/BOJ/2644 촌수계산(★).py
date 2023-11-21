def find(a):
    visited = [0]*(n+1)
    visited[a] = 1
    queue = deque([a])
    while queue:
        p = queue.popleft()
        for i in graph[p]:
            if not visited[i]:
                visited[i] = visited[p] + 1
                queue.append(i)

    return visited[c]-1


import sys
from collections import deque
n = int(sys.stdin.readline())
r, c = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

print(find(r))
