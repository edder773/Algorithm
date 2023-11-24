def find(n):
    visited[n] = 1
    for i in graph[n]:
        if not visited[i]:
            find(i)

import sys
N = int(sys.stdin.readline())
tree = list(map(int, sys.stdin.readline().split()))
d = int(sys.stdin.readline())
graph = [[] for _ in range(N)]
visited = [0]*(N)
for i in range(N):
    if tree[i] != -1 and i != d:
        graph[tree[i]].append(i)
find(d)

result = 0
for i in range(N):
    if not visited[i] and not graph[i] :
        result +=1
print(result) 