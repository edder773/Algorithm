import sys
N = int(sys.stdin.readline())
x = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)])
y = [1]*N

# 교차하는 횟수가 1번이라도 있는 전깃줄 제거
# x의 [i][1]인덱스와 x의[j][1] 인덱스들을 하나씩 비교

for i in range(N):
    for j in range(i):
        if x[i][1] > x[j][1]:
            y[i] = max(y[i], y[j]+1)
print(N-max(y))
