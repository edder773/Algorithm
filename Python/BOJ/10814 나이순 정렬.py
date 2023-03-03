import sys
N = int(sys.stdin.readline())
P = [0]*N
for i in range(N) :
    x = list(map(str,sys.stdin.readline().split()))
    P[i] = (int(x[0]),x[1])
P.sort(key = lambda a:a[0])
for j in P :
    print(j[0],j[1])