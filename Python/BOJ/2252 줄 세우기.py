import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
visited = [0]*(N+1)
student = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    student[a].append(b)
    visited[b] += 1

# 여기서부터 위상 정렬
result = []
queue = deque()

for i in range(1, N+1):
    if not visited[i]:
        queue.append(i)

while queue:
    now = queue.popleft()
    result.append(now)
    for i in student[now]:
        visited[i] -= 1
        if not visited[i] :
            queue.append(i)
print(*result)