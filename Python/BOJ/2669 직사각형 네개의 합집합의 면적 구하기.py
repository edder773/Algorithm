import sys
graph =[[0]*101 for _ in range(101)]

for _ in range(4):
    x, y, nx, ny = map(int, sys.stdin.readline().split())
    for i in range(x,nx):
        for j in range(y,ny):
            graph[i][j] = 1

result = 0
for i in range(101):
    for j in range(101):
        if graph[i][j] == 1:
            result += 1
print(result)