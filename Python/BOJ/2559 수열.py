import sys
N, K = map(int, sys.stdin.readline().split())
temper = [0]+list(map(int, sys.stdin.readline().split()))
y = []
for i in range(1, N+1):
    temper[i] += temper[i-1]

for j in range(K, N+1):
    y.append(temper[j] - temper[j-K])
print(max(y))
