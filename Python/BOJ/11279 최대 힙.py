import sys, heapq
N = int(sys.stdin.readline())
queue = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if n :
        heapq.heappush(queue, -n)
    elif not queue and n == 0:
        print(0)
    else :
        print(-heapq.heappop(queue))