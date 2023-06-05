import sys, heapq
N = int(sys.stdin.readline())
min_heap = [] # 최소힙과
max_heap = [] # 최대힙으로 나누자
for _ in range(N):
    x = int(sys.stdin.readline())
    if len(max_heap) == len(min_heap): #둘의 길이가 같으면
        heapq.heappush(max_heap, (-x,x)) # 최대 힙에 넣고 (최대힙의 첫 값은 중앙값!)
    else : # 다르면
        heapq.heappush(min_heap, (x,x)) #최소 힙에 넣자
    if min_heap and max_heap[0][1] > min_heap[0][1]: # 최소 힙이 존재하고, 각 첫번째 원소 중에 최대 힙이 더 크면
        min_x, max_x = heapq.heappop(min_heap)[1], heapq.heappop(max_heap)[1] # 각각 우선 순위 높은걸 꺼내서
        heapq.heappush(max_heap, (-min_x, min_x)), heapq.heappush(min_heap, (max_x, max_x))# 각각에 바꿔 넣자
    print(max_heap[0][1])