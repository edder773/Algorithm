def find(n):
    if visited[n]:
        return False
    visited[n] = 1
    for i in team[n]:
        if not troll[i] or find(troll[i]):
            troll[i] = n
            return True
    return False

import sys
N, M, K1, K2 = map(int, sys.stdin.readline().split()) # 사람, 트롤, 트롤수들
result = []
for case in (K1, K2): # K1, K2개의 팀에 해당하는 케이스
    team = [[] for _ in range(N+1)]
    for _ in range(case):
        a, b = map(int, sys.stdin.readline().split())
        team[a].append(b)

    troll = [0]*(M+1)
    cnt = 0
    for i in range(1, N+1):
        visited = [0] * (N+1)
        if find(i):
            cnt += 1
    result.append(cnt)
    
if result[0] < result[1]:
    print('네 다음 힐딱이')
else:
    print('그만 알아보자')