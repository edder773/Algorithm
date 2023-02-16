T = int(input())
for case in range(1, T+1):
    try:
        x = list(input().split())
        stack = []
        for i in x:
            if i == '+':
                stack.append(stack.pop()+stack.pop())
            elif i == '-':
                minus = stack.pop()
                stack.append(stack.pop()-minus)
            elif i == '*':
                stack.append(stack.pop()*stack.pop())
            elif i == '/':
                div = stack.pop()
                stack.append(stack.pop()//div)
            elif i == '.':
                if len(stack) == 1:
                    print(f'#{case}', *stack)
                else:
                    print(f'#{case}', error)
            else:
                stack.append(int(i))  # 숫자 입력시 stack에 숫자 입력
    except:
        print(f'#{case} error')  # 에러 발생시 error 출력
