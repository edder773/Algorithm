T = int(input())
for _ in range(T):
    N = int(input())
    p = [0]*100
    p[0] = 1
    p[1] = 1
    p[2] = 1
    p[3] = 2
    p[4] = 2
    for i in range(95):
        p[i+5] = p[i] + p[i+4]
    print(p[N-1])
