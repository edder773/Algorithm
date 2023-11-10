import sys
T = int(sys.stdin.readline())
for _ in range(T):
    J, N = map(int, sys.stdin.readline().split())
    box = []
    for _ in range(N):
        R, C = map(int, sys.stdin.readline().split())
        box.append(R*C)
    box.sort(reverse=True)
    result = 0
    for i in range(N):
        if box[i] <= J:
            J -= box[i]
            result += 1
        else:
            if J :
                result += 1
            break
    print(result)
