def find(n):
    if visited[n]:
        return False
    visited[n] = 1
    for i in graph[n]:
        if not selected[i] or find(selected[i]):
            selected[i] = n
            return True
    return False

import sys
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
selected = [0] * (M+1)
for i in range(1,N+1):
    graph[i] = list(map(int, sys.stdin.readline().split()))[1:]

for i in range(1,N+1):
    visited = [0]*(N+1)
    find(i)

result = 0
for i in range(1, M+1):
    if selected[i]:
        result += 1
print(result)