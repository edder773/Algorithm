def add(arr):
    m, result = len(arr), []
    for i in range(m+1):
        for x in combinations(arr, i):
            result.append(sum(x))
    return result

import sys
from itertools import combinations
N, C = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))
mid = N // 2
left, right = items[:mid], items[mid:]
L, R = sorted(add(left)), add(right)
result = 0

for i in R:
    if i > C:
        continue
    start, end = 0, len(L) - 1
    while start <= end :
        mid = (start + end) // 2
        if L[mid] + i > C:
            end = mid - 1
        else:
            start = mid + 1
    result += end + 1
print(result)