T = int(input())
for case in range(1,T+1):
    stack = []
    x = list(input())
    for i in x :
        if len(stack) >= 1 and stack[-1] == i: #스택길이가 2이상이고 마지막과 입력이 같으면
            stack.pop()
        else :
            stack.append(i)
    print(f'#{case} {len(stack)}')
