import sys
N = int(sys.stdin.readline().strip())
x = [*map(int, sys.stdin.readline().split())]
M = int(sys.stdin.readline().strip())
y = [*(map(int, sys.stdin.readline().split()))]

cnt = {}
for i in x:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for j in y:
    a = cnt.get(j)
    if a == None:
        print(0, end=' ')
    else:
        print(a, end=' ')
