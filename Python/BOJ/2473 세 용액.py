import sys
N = int(sys.stdin.readline())
liquid = sorted(list(map(int, sys.stdin.readline().split())))

x = float('inf')
for i in range(N-1):
    start, end = i+1, N- 1
    while start < end:
        mid = liquid[i] + liquid[start] + liquid[end]
        if abs(mid) < x:
            x = abs(mid)
            result = [liquid[i], liquid[start], liquid[end]]
            if x == 0 :
                break
        elif mid < 0:
            start += 1
        else :
            end -= 1
print(*result)