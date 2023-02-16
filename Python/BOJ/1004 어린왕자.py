import sys
T = int(sys.stdin.readline())
for _ in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    cnt = 0
    for _ in range(n):
        Cx, Cy, r = map(int, sys.stdin.readline().split())
        distance_start = ((Cx-x1)**2+(Cy-y1)**2)**(1/2)
        distance_end = ((Cx-x2)**2+(Cy-y2)**2)**(1/2)
        if (distance_start < r and distance_end > r) or (distance_start > r and distance_end < r):
            cnt += 1
    print(cnt)
