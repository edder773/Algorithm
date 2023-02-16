T = int(input())


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


for case in range(1, T+1):
    V, E = map(int, input().split())
    x = [[] for _ in range(V+1)]
    visited = [False] * len(x)
    for i in range(E):
        a, b = map(int, input().split())
        x[a] += [b]  # 이어져있는 노드 생성
    S, G = map(int, input().split())  # S 시작 G 끝
    dfs(x, S, visited)  # S부터 시작해서 방문 가능한 노드 확인
    if visited[G] == True:  # 만약 G를 방문했다면
        print(f'#{case} {1}')
    else:
        print(f'#{case} {0}')
