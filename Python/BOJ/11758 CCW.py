def CCW(a,b,c):
    result = (a[1]*b[0] + b[1]*c[0] + c[1]*a[0]) - (a[0]*b[1] +b[0]*c[1] + c[0]*a[1])
    if result > 0 : #시계 방향
        return 1
    elif result == 0 : # 일직선
        return 0
    else : # 반시계 방향
        return -1

import sys
point = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
print (CCW(point[1],point[0],point[2]))