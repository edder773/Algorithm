import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    stuck = list(map(int, sys.stdin.readline().split()))
    result, value = 0, 0
    for i in range(N-1, -1, -1):
        if(value < stuck[i]):
            value = stuck[i]
        else:
            result += value - stuck[i]
    print(result)