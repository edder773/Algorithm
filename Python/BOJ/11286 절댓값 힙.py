import sys, heapq
N = int(sys.stdin.readline())
queue = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x :
        heapq.heappush(queue, [abs(x), x])
    elif not queue and x == 0: 
        print(0)
    else :
        print(heapq.heappop(queue)[1])