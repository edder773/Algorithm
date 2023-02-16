import sys
N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))
O = list(sorted(set(X)))

y = {O[i]: i for i in range(len(O))}

for i in X:
    print(y[i], end=' ')
