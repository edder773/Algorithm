import sys
A, B = sys.stdin.readline().strip().split()
n, m = len(A), len(B)
result = int(10e9)
for i in range(m-n+1):
    temp = 0
    for j in range(n):
        print(A[j], B[i+j])
        if A[j] != B[i+j]:
            temp += 1
    result = min(result, temp)
print(result)