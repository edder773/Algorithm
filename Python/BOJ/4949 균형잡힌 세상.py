while True:
    x = input()
    if x == '.':
        break
    stack = []
    for i in x:
        if i == '(' or i == ')' or i == '[' or i == ']':
            stack.append(i)

        if len(stack) >= 2 and ((stack[-1] == ')' and stack[-2] == '(') or (stack[-1] == ']' and stack[-2] == '[')):
            stack.pop()
            stack.pop()
    if stack:
        print('no')
    else:
        print('yes')
