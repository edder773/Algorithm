def one_num(n):
    p = []
    for j in range(100, int(n+1)):
        x = list(str(j))
        y = 0
        for i in range(len(x)):
            y += int(x[i])
        if int(x[len(x)//2])*3 == y:
            p.append(j)

    if n < 100:
        return n

    return len(p)+99


n = int(input())
print(one_num(n))
