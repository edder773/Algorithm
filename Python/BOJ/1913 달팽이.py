import sys
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
dy = [1,0,-1,0]
dx = [0,1,0,-1]
snail = [[0]*N for _ in range(N)]
d =0
y,x = 0,0
for i in range(N*N,0,-1):
    if i == K:
        result_y, result_x = y+1, x+1
    snail[y][x] = i
    ny, nx = y +dy[d], x + dx[d]
    if 0 <= ny < N and 0 <= nx < N and snail[ny][nx] == 0:
        y, x = ny, nx
    else:
        d = (d+1) % 4
        y, x = y + dy[d], x + dx[d]

for x in snail:
    print(*x)
print(result_y,result_x)