def self_num(n):
    x = list(str(n))
    y = 0
    for i in range(len(x)):
        y += int(x[i])
    z = y + n
    return z


p = []
for i in range(10000):
    p.append(self_num(i))
O = set(p)
for j in range(1, 10001):
    if j not in O:
        print(j)
