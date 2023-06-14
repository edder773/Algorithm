# 트리의 지름 - > 임의의 두 점 사이의 거리 중 가장 긴 것
# 즉, 특정 노드에서 가장 먼 노드를 찾은 후, 해당 지점에서 다시 가장 먼 노드 까지의 거리를 구하면 된다.

def find(start, now):
    for a, b in graph[start]:
        if not visited[a]:
            visited[a] = now + b
            find(a, now + b)

import sys
V = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    tree = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(tree)-2, 2):
        graph[tree[0]].append([tree[i], tree[i+1]])

visited = [0]*(V+1)
visited[1] = 1
find(1, 0) # 1번 노드에서 가장 먼 노드를 찾자 (1번 아니어도 됨)

start = visited.index(max(visited)) # 1번 노드에서 가장 먼 노드를 다시 찾자.
visited = [0]*(V+1)
visited[start] = 1
find(start, 0) # 1번 노드에서 가장 먼 노드에서 제일 먼 노드 재 탐색

print(max(visited))