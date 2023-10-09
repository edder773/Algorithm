import sys
N, M = map(int, sys.stdin.readline().split())
j = int(sys.stdin.readline())
move = 0
start,end = 1, M
for _ in range(j):
    x = int(sys.stdin.readline())
    if x < start:
        move += (start-x)
        start = x
        end = x + M - 1
    elif x > end :
        move += (x - end)
        end = x
        start = end - M + 1
print(move)