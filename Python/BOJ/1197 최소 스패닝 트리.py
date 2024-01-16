def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

import sys
V, E = map(int, sys.stdin.readline().split())
parent = [0] * (V+1)
for i in range(1, V+1):
    parent[i] = i

cost = 0
line = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(E)], key = lambda x : x[2])
for a, b, c in line:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        cost += c
print(cost)