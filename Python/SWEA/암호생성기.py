for case in range(1,11):
    T = int(input())
    x = list(map(int, input().split()))
    while True:
        if x[-1] == 0:
            break
        else :
            for i in range(1,6): # 1~5를
                a = x.pop(0) #맨앞에꺼 꺼낸거에서
                if a-i > 0: #0 이상일때만
                    x.append(a-i) #빼서 뒤에 넣으세요
                else :
                    x.append(0)
                    break
    print(f'#{case}',*x)