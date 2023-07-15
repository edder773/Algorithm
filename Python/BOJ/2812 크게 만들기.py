import sys
N, K = map(int, sys.stdin.readline().split())
x = list(map(int, sys.stdin.readline().strip()))
stack = []

for i in x:
    while stack and K and stack[-1] < i:
        stack.pop()
        K -= 1
    stack.append(i)
if K:
    print(*stack[:-K], sep="")
else:
    print(*stack, sep="")