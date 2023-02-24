N = int(input())
x = [0]*N
for i in range(N):
    x[i] = int(input())
com = x[-1]
cnt = 1

for i in reversed(x):
    if com < i :
        cnt += 1
        com = i
print(cnt)