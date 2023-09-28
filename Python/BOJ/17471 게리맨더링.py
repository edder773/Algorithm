# 조건 1 : 선거구를 2개로 나눈다. -> 나누는 과정에서 가능한 조합을 찾는다
# 조건 2 : 각 구역은 선거구 중 하나에 포함되어야 한다.
# 조건 3 : 선거구에 포함된 구역은 모두 연결되야한다.
# 조건 4 : 인구 차이의 최소를 구하자
def bfs(n):
    visited = [n[0]]
    queue = deque()
    queue.append(n[0])
    result = 0
    while queue:
        a = queue.popleft()
        result += area[a]
        for i in near[a]:
            if i not in visited and i in n:
                queue.append(i)
                visited.append(i)
    return result, len(visited)

import sys
from collections import deque
from itertools import combinations
N = int(sys.stdin.readline())
area = list(map(int, sys.stdin.readline().split()))
near = [[]*N for _ in range(N+1)]
for i in range(1,N+1):
    M, *site = map(int, sys.stdin.readline().split())
    for j in site:
        near[i].append(j)

lines = [i for i in range(N)]
result = float('inf')
for i in range(1, N//2+1):
    comb = list(combinations(lines,i))
    for j in comb:
        temp2 = []
        a1, b1 = bfs(j)
        for k in lines:
            if k not in comb:
                temp2.append(k)
        a2, b2 = bfs(temp2)
        if b1 + b2 == N :
            result = min(result,abs(a1-a2))
if result == float('inf'):
    print(-1)
else:
    print(result)