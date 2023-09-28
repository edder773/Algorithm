import sys
from collections import deque

N = int(sys.stdin.readline())
balloon = list(map(int, sys.stdin.readline().split()))
queue = deque()

for i in range(1, N + 1):
    queue.append([i, balloon[i - 1]])

result = []
while queue:
    a, b = queue.popleft()
    result.append(a)
    if b > 0:
        queue.rotate(1 - b)
    else:
        queue.rotate(-b)
print(*result)
