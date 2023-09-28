import sys
N = int(sys.stdin.readline())
stack = []
for i in range(N):
    x = list(map(int, sys.stdin.readline().split()))
    if x[0] == 1:
        stack.append(x[1])
    elif x[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif x[0] == 3:
        print(len(stack))
    elif x[0] == 4:
        if stack:
            print(0)
        else:
            print(1)
    elif x[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)