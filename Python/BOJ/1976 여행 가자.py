def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
parent = [i for i in range(N+1)]

for i in range(1,N+1):
    link = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if link[j]:
            union(i,j+1)

plan = list(map(int, sys.stdin.readline().split()))
start = parent[plan[0]]
result = 'YES'
for i in plan:
    if start != parent[i]:
        reault = 'NO'
        break
print(result)