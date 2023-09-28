import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
bus = [[10e9 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    bus[a][b] = min(c, bus[a][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            bus[i][j] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            bus[i][j] = min(bus[i][j],
                                    bus[i][k] + bus[k][j])


result = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if bus[i+1][j+1] != 10e9:
            result[i][j] = bus[i+1][j+1]

for i in result:
    print(*i)