import sys
N, K = map(int, sys.stdin.readline().split())
x = [0]*N
cnt = 0
for t in range(N):
    x[t] = int(sys.stdin.readline())

for i in range(N-1, -1, -1):
    if K // x[i] > 0:
        cnt += K // x[i]
        K = K % x[i]
    if K == 0:
        break
print(cnt)
