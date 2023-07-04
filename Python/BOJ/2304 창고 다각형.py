import sys
N = int(sys.stdin.readline())
pole = [0]*1001
maxH, idx = 0, 0
for _ in range(N):
    L, H = map(int, sys.stdin.readline().split())
    pole[L] = H
    if maxH < H:
        maxH = H
        idx = L
result = 0

height = 0
for i in range(idx+1):
    height = max(height, pole[i])
    result += height

height = 0
for i in range(1000, idx, -1):
    height = max(height, pole[i])
    result += height

print(result)