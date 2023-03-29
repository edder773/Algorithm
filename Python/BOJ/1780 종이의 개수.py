def div(y,x,n):
    num = paper[y][x]
    for i in range(y,y+n):
        for j in range(x,x+n):
            if num != paper[i][j]:
                m = n//3 # 3분할 해보자
                div(y, x, m) 
                div(y, x + m, m)
                div(y, x + 2*m, m)
                div(y + m, x, m)
                div(y + m, x + m, m)
                div(y + m, x + 2*m, m)
                div(y + 2*m, x, m)
                div(y + 2*m, x + m, m)
                div(y + 2*m, x + 2*m, m) #여기까지 3분할씩 한 영역
                return
    if num == -1:
        result[0] += 1
    elif num == 0:
        result[1] += 1
    else :
        result[2] += 1 

import sys
N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = [0,0,0]
div(0,0,N)
for i in range(3):
    print(result[i])