def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

import sys
n = int(sys.stdin.readline())
stars = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]
edge = []
for i in range(n-1):
    for j in range(i+1, n):
        cost = ((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2)**(1/2)
        edge.append([cost,i,j])

edge.sort()

parent = [0]*(n+1)
parent = [i for i in range(n+1)]

result = 0
for cost, x , y in edge:
    if find(parent, x) != find(parent, y):
        union(parent, x, y)
        result += cost
print(round(result,2))