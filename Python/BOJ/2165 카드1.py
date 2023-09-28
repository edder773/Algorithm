import sys
from collections import deque
N = int(sys.stdin.readline())
queue = deque([i for i in range(1,N+1)])
result = []
while queue :
    result.append(queue.popleft())
    if queue:
        queue.append(queue.popleft())
print(*result)