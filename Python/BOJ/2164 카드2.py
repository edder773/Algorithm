import sys
from collections import deque
N = int(sys.stdin.readline())
X = deque(i for i in range(1, N+1))
while True:
    if N == 1:
        X = deque('1')
        break
    X.popleft()
    y = X[0]
    X.popleft()
    X.append(y)
    if len(X) == 1:
        break
print(*X)
