import sys
N, M, B = map(int,sys.stdin.readline().split())
block = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
height = 0
times = float('inf')
for i in range(257):
    m = n = 0
    for j in range(N):
        for k in range(M):
            if block[j][k] < i :
                n += (i - block[j][k])
            else:
                m += (block[j][k] -i)
    ven = B + m
    if ven < n:
        continue
    result = 2*m + n
    if times >= result:
        times= result
        height = i
print(times, height)