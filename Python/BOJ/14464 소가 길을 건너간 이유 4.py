import sys

C, N = map(int, sys.stdin.readline().split())
chicken = sorted([int(sys.stdin.readline()) for _ in range(C)])
cow = sorted(
    [list(map(int, sys.stdin.readline().split())) for _ in range(N)],
    key=lambda x: (x[1], x[0]),
)
visited = [0] * C
result = 0
for a, b in cow:
    for i in range(C):
        if a <= chicken[i] <= b and not visited[i]:
            result += 1
            visited[i] = 1
            break
print(result)
