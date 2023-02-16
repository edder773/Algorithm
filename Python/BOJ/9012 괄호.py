N = int(input())
for _ in range(N):
    x = list(input())
    stack = []
    for i in x:
        if i == '(' or i == ')':
            stack.append(i)
        if len(stack) >= 2 and (stack[-1] == ')' and stack[-2] == '('):
            stack.pop()
            stack.pop()
    # print(stack)
    if stack:
        print('NO')
    else:
        print('YES')
