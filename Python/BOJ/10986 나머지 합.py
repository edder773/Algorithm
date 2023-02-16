import sys
N, M = map(int, sys.stdin.readline().split())
x = list(map(int, sys.stdin.readline().split()))+[0]
r = [0]*M
for i in range(N):
    x[i] += x[i-1]
    r[x[i] % M] += 1
cnt = r[0]

for i in r:
    cnt += i*(i-1)//2

print(r)
print(cnt)
