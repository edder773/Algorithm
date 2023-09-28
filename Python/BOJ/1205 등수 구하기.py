import sys
N, score, P = map(int, sys.stdin.readline().split())
if N == 0:
    print(1)
else:
    nums = list(map(int, sys.stdin.readline().split()))
    if N == P and nums[-1] >= score:
        print(-1)
    else:
        result = N + 1
        for i in range(N):
            if nums[i] <= score:
                result = i + 1
                break
        print(result)