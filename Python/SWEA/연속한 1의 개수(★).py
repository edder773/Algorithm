T = int(input())


def max_case(n):
    cnt = n[0]
    for i in range(len(n)):
        if cnt < n[i]:
            cnt = n[i]
    return cnt


for case in range(1, T+1):
    N = int(input())
    x = list(input())
    temp = []
    cnt = 1
    for i in range(N):
        if (x[0] != x[N-1]) or (x[0] == '0' and x[N-1] == '0'):
            if x[i-1] == '1' and x[i] == '1':
                cnt += 1
                temp += [cnt]
            elif x[i-1] != x[i]:
                cnt = 1
            else:
                temp += [1]
    print(f'#{case} {max_case(temp)}')
