import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
for _ in range(N):
    A = sys.stdin.readline().split()
    if A[0] == 'push_front':
        queue.appendleft(A[1])
    elif A[0] == 'push_back':
        queue.append(A[1])

    elif A[0] == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else :
            print(queue.popleft())
    
    elif A[0] == 'pop_back':
        if len(queue) == 0:
            print(-1)
        else :
            print(queue.pop())

    elif A[0] == 'size':
        print(len(queue))
    elif A[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else :
            print(0)
    elif A[0] == 'front':
        if len(queue) == 0 :
            print(-1)
        else:
            print(queue[0])
    elif A[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])