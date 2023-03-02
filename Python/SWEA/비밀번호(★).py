for case in range(1,11):
    N, M = input().split()
    password = list(M)
    stack = []
    for i in password:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    print(f'#{case}', ' ', *stack, sep='')