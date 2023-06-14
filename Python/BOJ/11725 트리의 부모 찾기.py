import sys
N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
visited = [0]*(N+1)
result = [0]*(N+1)
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

visited[1] = 1
stack = [1]
while stack:
    x = stack.pop()
    for i in tree[x]:
        if not visited[i]:
            stack.append(i)
            visited[i] = 1
            result[i] = x
            
for i in result[2:]:
    print(i)