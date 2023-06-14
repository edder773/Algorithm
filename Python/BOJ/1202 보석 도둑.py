import sys, heapq
N, K = map(int, sys.stdin.readline().split())
gem = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)])
bag = sorted([int(sys.stdin.readline()) for _ in range(K)])
result = 0
heap = []
for i in bag:
    while gem and gem[0][0] <= i: # 보석이 남아있고, 무게가 bag보다 작은 동안
        heapq.heappush(heap, -gem[0][1]) # 가격을 넣고
        heapq.heappop(gem) # 보석을 빼자
    if heap: # heap에 들어 있으면
        result -= heapq.heappop(heap) # 가장 우선 순위 높은것 1개를 넣자 (가방 갯수만큼 반복)
print(result)
