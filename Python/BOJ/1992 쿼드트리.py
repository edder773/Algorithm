def tree(y,x,n):
    global result
    color = data[y][x]
    for i in range(y,y+n):
        for j in range(x,x+n):
            if color != data[i][j]:
                m = n//2
                result += '(' 
                tree(y, x, m) # 왼쪽 위 (2사분면)
                tree(y, x+m, m) # 오른쪽 위 (1사분면)
                tree(y+m, x, m) # 왼쪽 아래 (3사분면)
                tree(y+m, x+m, m) # 오른쪽 아래 (4사분면)
                result += ')'
                return
    if color == 1: # 영역이 1이면
        result += str(1) # 1 표시
    else : # 영역이 0 이면
        result += str(0) # 0 표시

import sys
N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
result = ''
tree(0,0,N)
print(result)