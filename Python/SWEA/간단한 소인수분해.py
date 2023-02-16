T = int(input())
for case in range(1, T+1):
    N = int(input())
    num = [2, 3, 5, 7, 11]
    temp = [0]*5
    cnt = 0
    while True:
        if N == 1:
            break
        for i in range(5):
            if N % num[i] == 0:
                N = N//num[i]
                temp[i] += 1
                break
    print(f'#{case}', *temp)
