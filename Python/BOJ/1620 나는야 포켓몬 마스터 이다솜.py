import sys
N, M = map(int, sys.stdin.readline().split())
poket = {}
poket2 = {}

for i in range(N):
    n = sys.stdin.readline().strip()
    poket[i] = n
    poket2[n] = i

for k in range(M):
    m = sys.stdin.readline().strip()
    if (m.isdigit() == True):
        print(poket[int(m)-1])
    else:
        print(poket2[m]+1)
