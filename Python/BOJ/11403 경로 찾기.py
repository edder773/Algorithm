import sys
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if graph[j][i] == 1 and graph[i][k] == 1:
                graph[j][k] = 1

for i in graph:
    print(*i)