import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline())
check, result = [], []
for _ in range(N):
    n, start, end = map(int, sys.stdin.readline().split())
    heappush(check,(start,end))

start, end = heappop(check)
heappush(result, end)

while check:
    start, end = heappop(check)
    if result[0] <= start:
        heappop(result)
    heappush(result,end)

print(len(result))