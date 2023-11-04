import sys
N = int(sys.stdin.readline())
sell = {}
for _ in range(N):
    book = sys.stdin.readline().strip()
    if book not in sell :
        sell[book] = 0
    sell[book] += 1
result = []
for i in sell :
    if sell[i] == max(sell.values()):
        result.append(i)
result.sort()
print(*result[:1])