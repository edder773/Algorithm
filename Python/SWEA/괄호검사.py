T = int(input())
for case in range(1, T+1):
    x = list(input())
    stack = []
    for i in x:
        if i == '(' or i == ')' or i == '{' or i == '}':
            stack.append(i)
            if len(stack) >= 2:  # 스택 길이가 2고
                # 들어온 괄호와 앞의 괄호의 짝이 맞으면
                if (stack[-1] == ')' and stack[-2] == '(') or (stack[-1] == '}' and stack[-2] == '{'):
                    stack.pop()
                    stack.pop()
    if len(stack) == 0:
        print(f'#{case} {1}')
    else:
        print(f'#{case} {0}')
