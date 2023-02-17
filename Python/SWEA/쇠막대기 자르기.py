T = int(input())
for case in range(1, T+1):
    x = input()
    result = cnt = 0 # 토막 갯수, 막대 갯수
    for i in range(len(x)):
        if x[i] == '(':
            cnt += 1
        else:
            if x[i-1] == '(':
                cnt -= 1
                result += cnt
            else:
                cnt -= 1
                result += 1
    print(f'#{case} {result}')