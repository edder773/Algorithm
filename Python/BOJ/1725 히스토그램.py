def compare(n):
    global result
    h = height[stack[-1]]
    stack.pop()
    x = n
    if stack:
        x = (n-1 - stack[-1])
    result = max(result, x*h)

    

import sys
N = int(sys.stdin.readline())
height = [int(sys.stdin.readline()) for _ in range(N)]
result = 0

stack = []
for i in range(N):
    while stack and height[stack[-1]] > height[i]:
        compare(i)
    stack.append(i)

# while stack:
#     compare(i)

print(result)
