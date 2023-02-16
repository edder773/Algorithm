N = input()


def m(n):
    X = list(str(n))
    a = 0
    for i in X:
        a += int(i)
    return int(n) + a


temp = []
for i in range(int(N)):
    temp.append(m(i))
if int(N) in temp:
    print(temp.index(int(N)))
else:
    print(0)
