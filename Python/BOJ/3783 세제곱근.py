def find(x):
    start, end = 0, x
    while start < end:
        mid = (start+end) // 2
        if mid ** 3 == x:
            return mid
        elif mid ** 3 < x:
            start = mid + 1
        elif mid ** 3 > x:
            end = mid - 1
    return end

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    if n == 0 :
        print(f'{n:.10f}')
    else :
        n *= 10**30
        a = str(find(n))
        b = len(a)
        print(f'{a[:b-10]}.{a[-10:]}')