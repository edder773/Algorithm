for case in range(1,11):
    N = int(input())
    x = list(input())
    stack = []
    result = ''
    for i in x:
        if i == '+': # +를 만나면
            while stack : #stack이 빌때 까지
                result += stack.pop() # result에 stack을 pop한 결과물입력
            stack.append(i)
        elif i == '*' :
            while stack and stack[-1] == '*':
                result += stack.pop()
            stack.append(i)
        else:
            result += i
    while stack: #stack이 빌떄까지
        result += stack.pop()  #result에 stack을 pop한 결과물 입력
    stack = []
    for j in result:
        if j == '+': #더하기
            stack.append(stack.pop()+stack.pop())
        elif j == '*':
            stack.append(stack.pop()*stack.pop())
        else:
            stack.append(int(j))
    print(f'#{case} {stack[-1]}')
