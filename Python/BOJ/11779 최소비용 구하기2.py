def find(start):
    queue = [[0,start]]

    while queue:
        now, next = heappop(queue) 
        if distance[next] < now:
            continue

        for anext, anow in graph[next]:
            d = now + anow 
            if distance[anext] > d: 
                distance[anext], node[anext] = d, next
                heappush(queue, [d, anext]) 

import sys
from heapq import heappop, heappush
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v,w])

start, end = map(int, sys.stdin.readline().split())
distance = [10e9] *(N+1)
node = [start]*(N+1)
find(start)

result = []
x = end
while x != start :
   result.append(x)
   x = node[x]

result.append(start)
result.reverse()

print(distance[end])
print(len(result))
print(*result)