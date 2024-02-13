def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
        return parent[x]
    else:
        return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

import sys
N, Q = map(int, sys.stdin.readline().split())
log = []
for i in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    log.append([a,b,i+1])
log.sort()

parent = [i for i in range(N+1)]
x, y, d = log[0]
for i in range(1, N):
    nx, ny, nd = log[i]
    if nx <= y :
        union(d, nd)
        y = max(y, ny)
    else:
        x, y, d= nx, ny, nd

for _ in range(Q):
    a, b = map(int, sys.stdin.readline().split())
    if find(a) == find(b):
        print(1)
    else:
        print(0)