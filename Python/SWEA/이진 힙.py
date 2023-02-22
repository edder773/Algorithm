# def heaps(n): # 힙을 만들자
#     heap.append(n) # 힙에 n을 추가
#     idx = len(heap)-1 # 지금 들어온 n의 인덱스
#     while idx > 1 and heap[idx] < heap[idx//2]: # 인덱스가 1보다 크고 지금 들어온 인덱스가 부모 인덱스보다 더 작으면
#         heap[idx], heap[idx//2] = heap[idx//2], heap[idx] # 서로 자리를 바꿔준다
#         idx //= 2

# def heap_sum():
#     S = 0 
#     idx2 = N//2 
#     while idx2:
#         S += heap[idx2] # 마지막 노드 기준 조상 노드의 합
#         idx2 //= 2 #계속 2로 나눠준다.
#     return S

# T = int(input())
# for case in range(1,T+1):
#     N = int(input())
#     x = list(map(int, input().split()))
#     heap = [0]
#     for i in x: #힙에 받은 값하나 씩 넣어보자
#         heaps(i)
#     result = heap_sum() #완석된 힙의 조상 노드 합

#     print(f'#{case} {result}')

T = int(input())
for case in range(1,T+1):
    N = int(input())
    x = list(map(int, input().split()))
    heap = [0]
    sums = 0
    
    for i in x : # 리스트 요소에 대해
        heap.append(i) # 힙에 x 요소 넣기
        idx = len(heap)-1 # 들어온 요소의 인덱스
        while idx > 1 and heap[idx] < heap[idx//2]: #인덱스가 1보다 크고, 조상노드보다 새로 들어온게 작으면
            heap[idx], heap[idx//2] = heap[idx//2], heap[idx] # 계속 위치 바꿔주기
            idx //= 2
    
    idx = N//2 #조상 노드로 만들어주기
    while idx: 
        sums += heap[idx] #조상노드들의 합
        idx //= 2
    print(f'#{case} {sums}')