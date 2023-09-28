import sys
L = int(sys.stdin.readline())
S = [0] + sorted(list(map(int, sys.stdin.readline().split())))
n = int(sys.stdin.readline())
for i in range(L):
    if S[i] == n or S[i+1] == n:
        print(0)
        break
    elif S[i] < n < S[i+1]:
        print((n-S[i]) * (S[i+1] -n) - 1)
        break