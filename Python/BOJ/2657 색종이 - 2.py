import sys
N = int(sys.stdin.readline())
paper = [[0]*102 for _ in range(102)]
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            paper[i][j] = 1

move = [[0,1],[0,-1],[1,0],[-1,0]]

result = 0
for i in range(101):
    for j in range(101):
        if paper[i][j] == 1:
            for dy, dx in move:
                ny, nx = i + dy, j + dx
                if paper[ny][nx] == 0 :
                    result += 1
print(result)
