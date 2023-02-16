import sys
N = int(sys.stdin.readline())
stack = []
for i in range(N):
    x = list(sys.stdin.readline().split())
    if x[0] == 'push':
        stack.append(x[1])
    elif x[0] == 'top':
        print(stack[-1])
    elif x[0] == 'size':
        print(len(stack))
    elif x[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif x[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
