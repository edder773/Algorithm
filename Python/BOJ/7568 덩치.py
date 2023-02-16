import sys

N = int(sys.stdin.readline())
temp = [0]*N
for i in range(N):
    x, y = tuple(map(int, sys.stdin.readline().split()))
    temp[i] = (x, y)

for k in range(N):
    cnt = 1
    for j in range(N):
        if (temp[k][0] != temp[j][0] and temp[k][0] != temp[j][0]):
            if (temp[k][0] < temp[j][0]) and (temp[k][1] < temp[j][1]):
                cnt += 1
    print(cnt, end=' ')
