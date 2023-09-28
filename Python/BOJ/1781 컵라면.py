import sys
from heapq import heappop, heappush
N = int(sys.stdin.readline())
cup = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)])

result = []
for dead, ramen in cup:
    heappush(result, ramen)
    if dead < len(result):
        heappop(result)
print(sum(result))