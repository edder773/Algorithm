T = int(input())
def bfs(n):
    queue = []
    queue.append(n)
    visited[n] = 1
    while queue:
        t = queue.pop(0)
        for i in graph[t]: # 정점에 대해
            if not visited[i]: # 방문 안했으면
                queue.append(i) #큐에 넣기
                visited[i] = visited[t]+1 # t로부터 1만큼 이동
    if visited[G] == 0: # 종점이 안이어져있으면
        return 0
    else :
        return visited[G] - 1

for case in range(1,T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    S, G = map(int, input().split())
    visited = [0]*(V+1)
    print(f'#{case} {bfs(S)}')