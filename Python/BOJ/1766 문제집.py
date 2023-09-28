import sys
from heapq import heappop, heappush

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
queue = []

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    visited[B] += 1

for i in range(1, N + 1):
    if not visited[i]:
        heappush(queue, i)

result = []
while queue:
    x = heappop(queue)
    result.append(x)
    for i in graph[x]:
        visited[i] -= 1
        if not visited[i]:
            heappush(queue, i)
print(*result)
