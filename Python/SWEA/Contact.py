def bfs(n):
    visited = [0]*101
    queue = []
    queue.append(n)
    visited[n] = 1
    while queue:
        a = queue.pop(0)
        for i in graph[a]:
            if not visited[i] :
                queue.append(i)
                visited[i] = visited[a] + 1
    # 가장 마지막에 연락받는 사람들의 index 모음 중에 가장 큰 index에 해당하는 값
    return max(list(filter(lambda x: visited[x] == max(visited), range(len(visited)))))


for case in range(1, 11):
    N, start = map(int, input().split())
    temp = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    for i in range(N//2):
        graph[temp[2*i]].append(temp[2*(i)+1])
    print(f'#{case} {bfs(start)}')
