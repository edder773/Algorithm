import sys
N, M = map(int, sys.stdin.readline().split())
A_temp = []
B_temp = []
C = []
for _ in range(N):
    A = list(map(int, input().split()))
    A_temp.append(A)
for _ in range(N):
    B = list(map(int, input().split()))
    B_temp.append(B)
for i in range(N):
    for j in range(M):
        print(A_temp[i][j] + B_temp[i][j], end=' ')
    print()
