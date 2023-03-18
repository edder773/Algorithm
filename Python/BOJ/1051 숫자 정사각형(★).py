import sys
N, M = map(int, sys.stdin.readline().split())
square = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
move = [[1,0], [1,1], [0,1]]
max_square = 1
for i in range(N):
    for j in range(M):
        for k in range(1,N):
            cnt = 0
            temp = square[i][j]
            for dy, dx in move :
                ny, nx = i + dy*k, j + dx*k
                if 0 <= ny < N and 0 <= nx < M:
                    if square[ny][nx] == temp:
                        cnt += 1
            if cnt == 3:
                max_square = max(max_square,(k+1)*(k+1))

print(max_square)

