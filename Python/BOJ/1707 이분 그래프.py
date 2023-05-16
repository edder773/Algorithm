def find(n):
    queue = deque([n])
    visited[n] = 1
    while queue: 
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i] : # 방문하지 않았으면
                visited[i] = -visited[x] # 이전 방문과 다른 색으로 표시 (1과 -1로 표시)
                queue.append(i)
            else:
                if visited[i] == visited[x]: # 다음 방문이 이전 방문과 같다면
                    return False
    return True

import sys
from collections import deque
K = int(sys.stdin.readline())
for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    for _ in range(E): # 그래프
        a, b = map(int,sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    result = 'YES'
    for i in range(1,V+1): # 각 정점에 대해
        if not visited[i]: # 방문하지 않았고
            if not find(i): # 탐색 했을 때 이분 그래프가 아니면
                result = 'NO' # NO 
                break
    print(result)