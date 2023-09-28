import sys
N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
result = 0

left, right = 0, 0

while right <= N:
    temp = sum(A[left:right])
    if temp == M:
        result += 1
        left += 1
    elif temp < M :
        right += 1
    else:
        left += 1
print(result)