K = int(input())
y = []  # 세로
x = []  # 가로
all = []  # 세로 + 가로
small = []
for i in range(6):
    n, m = map(int, input().split())
    all.append([n, m])
    if n == 1 or n == 2:
        x.append(m)
    else:
        y.append(m)

# 가장 긴 가로, 혹은 가장 긴 세로 변과 인접하지 않은 변의 길이 2개의 곱 = 작은 사각형
for i in range(6):
    if all[i][0] == all[(i+2) % 6][0]:
        small.append(all[(i+1) % 6][1])
print((max(x)*max(y) - small[0]*small[1])*K)
