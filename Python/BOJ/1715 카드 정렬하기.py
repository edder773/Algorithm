import sys, heapq
N = int(sys.stdin.readline())
result = 0
cards = []
for _ in range(N):
    heapq.heappush(cards, int(sys.stdin.readline()))
while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    result += (a+b)
    heapq.heappush(cards, a+b)
print(result)