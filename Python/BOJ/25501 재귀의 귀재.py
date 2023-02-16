T = int(input())


def recur(x, l, r):
    global cnt
    cnt += 1
    if l >= r:
        return 1
    elif x[l] != x[r]:
        return 0
    else:
        return recur(x, l+1, r-1)


def pal(x):
    return recur(x, 0, len(x)-1)


for _ in range(T):
    cnt = 0
    print(pal(input()), cnt)
