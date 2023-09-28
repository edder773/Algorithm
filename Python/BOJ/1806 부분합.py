import sys

N, S = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

result = float("inf")
left, right = 0, 0
x = 0
while True:
    if x >= S:
        result = min(result, right - left)
        x -= num[left]
        left += 1
    elif right == N:
        break
    else:
        x += num[right]
        right += 1

if result == float("inf"):
    result = 0
print(result)
