def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        cnt[a] += cnt[b]
    print(cnt[a])

def check(n):
    if n not in parent:
        parent[n] = n
        cnt[n] = 1

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    F = int(sys.stdin.readline())
    parent, cnt = {}, {}
    for __ in range(F):
        a, b = sys.stdin.readline().strip().split()
        check(a), check(b)
        union(a,b)