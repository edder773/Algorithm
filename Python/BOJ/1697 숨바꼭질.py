import sys
from collections import deque
N, K= map(int, sys.stdin.readline().split())
queue = deque()
queue.append(N)
way = [0]*100001 # 최대 크기

while queue:
    a= queue.popleft()
    if a == K: # 둘이 만났을 때
        print(way[a]) # 횟수 출력
        break

    for i in [a-1, a+1, a*2]:
        if 0 <= i < 100001 and way[i] == 0: #최대수보다 작고, 비었을 경우만 
            way[i] = way[a] + 1
            queue.append(i)