T = int(input())


def max_cnt(n):
    num = 0
    for value in range(len(n)):
        if int(n[value]) > num:
            num = int(n[value])
    return num


for case in range(1, T+1):
    N = int(input())
    card = list(input())
    temp = [0] * N
    max_cd = 0
    for i in range(N):
        for j in range(N):
            if card[i] == card[j]:
                temp[j] += 1

    for x in range(N):
        if (temp[x] == max_cnt(temp)):
            if card[x] > str(max_cd):
                max_cd = card[x]
        if max_cnt(temp) == 1:
            max_cd = max_cnt(card)

    print(f'#{case} {max_cd} {max_cnt(temp)}')
