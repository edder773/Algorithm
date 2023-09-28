def compare(n):
    global result
    h = height[stack[-1]]
    stack.pop()
    x = n
    if stack:
        x = (n-1 - stack[-1])
    result = max(result, x*h)

import sys
while True:
    n, *height= map(int, sys.stdin.readline().split())
    if n == 0:
        break

    stack= [] 
    result = 0
    for i in range(n):
        while stack and height[stack[-1]] > height[i]:
            compare(i)
        stack.append(i)

    while stack :
        compare(n)
    print(result)