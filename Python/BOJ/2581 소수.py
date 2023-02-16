M = int(input())
N = int(input())
p = []
cnt = 0
for i in range(M, N+1):
    y = 0
    if (i == 1):
        continue
    for j in range(2, i+1):
        if (i % j == 0):
            y += 1
    if (y == 1):
        p.append(i)
if p != []:
    print(sum(p))
    print(min(p))
else:
    print(-1)
