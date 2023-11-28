def union(a,b): # 합치기
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
def find(x): # 찾기
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

import sys
T = 1
while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    parent = [i for i in range(n+1)]
    cycle = set()
    for _ in range(m):
        a, b = map(int,sys.stdin.readline().split())
        if find(a) == find(b):
            cycle.add(parent[a])
            cycle.add(parent[b])

        if parent[a] in cycle :
            cycle.add(parent[b])
        
        if parent[b] in cycle:
            cycle.add(parent[a])

        union(a,b)

    for i in range(n+1):
        find(i)
    parent = set(parent[1:])

    result = 0
    for i in parent:
        if i not in cycle :
            result += 1

    if result == 0:
        print(f'Case {T}: No trees.')
    elif result == 1:
        print(f'Case {T}: There is one tree.')
    else:
        print(f'Case {T}: A forest of {result} trees.')
    T += 1