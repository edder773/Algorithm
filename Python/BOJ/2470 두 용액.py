import sys
N = int(sys.stdin.readline())
liquid = sorted(list(map(int, sys.stdin.readline().split())))
start, end = 0, N-1
result = [liquid[start], liquid[end]]
x = abs(liquid[start]+liquid[end])
while start < end:
    mid = liquid[start]+liquid[end]
    if abs(mid) < x:
        x = abs(mid)
        result = [liquid[start], liquid[end]]
        if x == 0:
            break
    elif mid < 0:
        start += 1
    else :
        end -= 1
print(*result)