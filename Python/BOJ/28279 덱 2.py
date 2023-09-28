import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
for _ in range(N):
    x = list(map(int, sys.stdin.readline().split()))
    if x[0] == 1:
        queue.appendleft(x[1])
    elif x[0] == 2:
        queue.append(x[1])
    elif x[0] == 3:
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif x[0] == 4:
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif x[0] == 5:
        print(len(queue))
    elif x[0] == 6:
        if queue:
            print(0)
        else:
            print(1)
    elif x[0] == 7:
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif x[0] == 8:
        if queue:
            print(queue[-1])
        else:
            print(-1)
