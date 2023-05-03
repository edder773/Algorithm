import sys
N = int(sys.stdin.readline())
cows = sorted([list(map(int,sys.stdin.readline().split())) for _ in range(N)])
cnt = 0 
for i in cows:
    if cnt < i[0]:
        cnt = i[0]
    cnt += i[1]
print(cnt)