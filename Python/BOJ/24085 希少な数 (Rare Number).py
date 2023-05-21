import sys
N = int(sys.stdin.readline())
num = sorted(list(map(int, sys.stdin.readline().split())))
x = {}
for i in num:
    if i in x:
        x[i] += 1
    else:
        x[i] = 1
print(min(x, key=x.get))