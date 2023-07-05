import sys
N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
B = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
result = 0
for i in range(N):
    result += A[i]*B[i]
print(result)