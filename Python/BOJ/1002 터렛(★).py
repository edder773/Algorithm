import sys
T = int(sys.stdin.readline())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    distance = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    if distance == 0 and r1 == r2:
        print(-1)
    elif abs(r1-r2) < distance < r1+r2:
        print(2)
    elif distance == r1 + r2 or abs(r1-r2) == distance:
        print(1)
    else:
        print(0)
