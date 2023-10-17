import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = sorted(list(map(int, sys.stdin.readline().split())))
    result = 0
    for i in A:
        left, right = 0, M-1
        temp = -1
        while left <= right:
            mid = (left + right)//2
            if B[mid] < i :
                left = mid + 1
                temp = mid
            else:
                right = mid - 1

        result += temp + 1
    print(result)