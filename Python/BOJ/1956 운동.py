import sys
V, E = map(int, sys.stdin.readline().split())
cycle = [[10e9]*(V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    cycle[a][b] = c

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            cycle[i][j] = min(cycle[i][j], cycle[i][k] + cycle[k][j])

result = 10e9
for i in range(1, V+1):
    result = min(result, cycle[i][i])

if result == 10e9 :
    result = -1
print(result)