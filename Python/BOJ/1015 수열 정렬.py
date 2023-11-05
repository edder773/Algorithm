import sys
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
B = sorted(A)
result = []
for i in range(N):
    idx = B.index(A[i])
    result.append(idx)
    B[idx] = -1
print(*result)