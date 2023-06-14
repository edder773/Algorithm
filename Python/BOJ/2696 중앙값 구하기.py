import sys, heapq
T = int(sys.stdin.readline())
for _ in range(T):
    M = int(sys.stdin.readline())
    if M % 10 == 0 :
        x = list(map(int, sys.stdin.readline().split()))
    else :
        x = []
        for _ in range(M//10 + 1):
            x += list(map(int, sys.stdin.readline().split()))
    heap_min, heap_max = [], []
    result = []
    cnt = 0
    for i in x:
        cnt += 1
        if len(heap_min) == len(heap_max): # 둘의 길이가 같으면
            heapq.heappush(heap_max, (-i, i)) # 최대 힙에 넣자
        else :
            heapq.heappush(heap_min, (i, i)) # 다르면 최소 힙에 넣자
        if heap_min and heap_max[0][1] > heap_min[0][1]: # 최소 힙이 존재하고, 각 첫 원소 중에 최대 힙이 더 크면
            minValue, maxValue = heapq.heappop(heap_min)[1], heapq.heappop(heap_max)[1] # 각각 우선 순위 높은걸 꺼내서
            heapq.heappush(heap_max, (-minValue, minValue)), heapq.heappush(heap_min, (maxValue, maxValue)) # 바꿔 넣자
        if cnt % 2 : # 홀 수 번째마다
            result.append(heap_max[0][1]) # 입력받은 중앙값 넣고

    print(len(result)) # 길이와
    for i in range(len(result)//10 + 1): # 10개 단위로 출력하자.
        print(*result[i*10:(i+1)*10])