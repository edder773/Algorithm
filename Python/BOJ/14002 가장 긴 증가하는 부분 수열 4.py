import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
x = [1] * N
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j] :
            x[i] = max(x[i], x[j]+1)
p = max(x)  
result = []
for i in range(N-1, -1, -1):
    if x[i] == p:
        result.append(A[i])
        p -= 1
result.reverse()
print(max(x))
print(*result)
