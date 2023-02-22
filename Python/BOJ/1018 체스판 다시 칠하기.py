import sys
N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline()) for _ in range(N)]
mincnt = float('inf') # 최소값
for i in range(N-7): 
    for j in range(M-7): #고려할 수 있는 범위
        x = y = 0 # 수정할 칸수
        for a in range(i,i+8): 
            for b in range(j,j+8): # 지정 8*8칸에 대해
                if (a+b) % 2 == 0: #시작이 W일때와 B일때 고려
                    if board[a][b] == 'W': 
                        x += 1
                    if board[a][b] == 'B':
                        y += 1
                else:
                    if board[a][b] == 'B':
                        x += 1
                    if board[a][b] == 'W':
                        y += 1
        if mincnt > x:
            mincnt = x
        if mincnt > y:
            mincnt = y
print(mincnt)
