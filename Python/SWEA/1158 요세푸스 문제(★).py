import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
queue = deque([i for i in range(1,N+1)])
print("<",end='')
while True:
    for _ in range(K-1):
        queue.append(queue.popleft())
    print(queue.popleft(),end='')
    if queue:
        print(', ',end='')
    else :
        break
print('>')