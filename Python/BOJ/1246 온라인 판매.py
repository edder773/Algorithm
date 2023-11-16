import sys
N, M = map(int, sys.stdin.readline().split())
P = sorted([int(sys.stdin.readline()) for _ in range(M)])
cost = 0
result = 0
for i in range(M):
    temp = M - i
    if N >= temp and P[i] * temp > result :
        cost = P[i]
        result = P[i] * temp
print(cost,result)