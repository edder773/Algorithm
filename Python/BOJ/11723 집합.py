import sys
N = int(sys.stdin.readline().strip())
S = set()
for _ in range(N):
    x = sys.stdin.readline().strip().split()
    if len(x) == 1:
        if x[0] == 'all':
            S = set([i for i in range(1,21)])
        else:
            S = set()

    if x[0] == 'add':
        S.add(int(x[1]))
    elif x[0] == 'remove':
        S.discard(int(x[1]))
    elif x[0] == 'check':
        if int(x[1]) in S:
            print(1)
        else:
            print(0)
    elif x[0] == 'toggle':
        if int(x[1]) in S:
            S.discard(int(x[1]))
        else :
            S.add(int(x[1]))