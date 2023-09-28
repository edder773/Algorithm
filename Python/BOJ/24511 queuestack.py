import sys
from collections import deque

N = int(sys.stdin.readline())
queuestack = list(map(int, sys.stdin.readline().split()))
num = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
insert = list(map(int, sys.stdin.readline().split()))
queue = deque()

for i in range(N):
    if queuestack[i] == 0:
        queue.appendleft(num[i])

result = []
for i in range(M):
    queue.append(insert[i])
    result.append(queue.popleft())
print(*result)
