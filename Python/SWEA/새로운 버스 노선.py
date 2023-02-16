T = int(input())

for case in range(1, T+1):
    N = int(input())
    s = [0] * N
    for num in range(N):
        s[num] = list(map(int, input().split()))
    stop = [i for i in range(1001)]
    temp = []

    for i in range(N):
        mum = []
        if s[i][0] == 1:
            temp += [stop[s[i][1]:s[i][2]+1]]
        if s[i][0] == 2:
            if s[i][1] % 2 == 0:
                temp += [stop[s[i][1]:s[i][2]+1:2] + [stop[s[i][2]]]]
            else:
                temp += [stop[s[i][1]:s[i][2]+1:2] + [stop[s[i][2]]]]
        if s[i][0] == 3:
            if s[i][1] % 2 == 0:
                alpa = stop[s[i][1]:s[i][2]]
                for i_x in range(len(alpa)):
                    if alpa[i_x] % 4 == 0:
                        mum += [alpa[i_x]]
                temp += [mum+[s[i][2]]]
            else:
                beta = stop[s[i][1]:s[i][2]]
                for i_y in range(len(beta)):
                    if beta[i_y] % 3 == 0 and beta[i_y] % 10 != 0:
                        mum += [beta[i_y]]
                temp += [mum+[s[i][2]]]
    stop_s = [0]*1010
    temp_c = []
    temp_d = []
    for t in range(len(temp)):
        for value in temp[t]:
            if value not in temp_c:
                temp_c.append(value)
        temp_d.append(temp_c)
        temp_c = []

    for j in range(N):
        for k in range(len(temp_d[j])):
            stop_s[temp_d[j][k]] += 1

    max_stop = stop_s[0]
    for t in range(len(stop_s)):
        if max_stop < stop_s[t]:
            max_stop = stop_s[t]

    print(f'#{case} {max_stop}')
