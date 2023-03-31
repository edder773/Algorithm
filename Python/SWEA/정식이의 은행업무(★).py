T = int(input())
for case in range(1, T+1):
    b = input() # 2진수
    t = input() # 3진수
    ts = ['0', '1', '2'] # 3진수 모음
    bs = [] # 2진수를 10진수로 바꾼 값 모음
    for i in range(len(b)): # 가능한 2진수 찾기
        if b[i] == '0':
            temp = b[:i] + '1' + b[i+1:]
            bs.append(int(temp, 2)) # 10진수로 변환해서 모으기
        else:
            temp = b[:i] + '0' + b[i+1:]
            bs.append(int(temp, 2))
    for i in range(len(t)):
        for j in ts:
            if t[i] != j:
                temp = t[:i] + j + t[i+1:] # 3진수도 하나씩 찾아보자
                if int(temp, 3) in bs: # 3진수를 10진수로 바꿔서 2진수 10진수로 바꾼거에 있으면
                    print(f'#{case} {int(temp, 3)}') #정답
