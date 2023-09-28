def union(a,b):
    a, b = find(a), find(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

import sys
sys.setrecursionlimit(100000)
n, m = map(int, sys.stdin.readline().split())
p = [i for i in range(n+1)]

for _ in range(m):
    x, a, b = map(int, sys.stdin.readline().split())
    if x == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')