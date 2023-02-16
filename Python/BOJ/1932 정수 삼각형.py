import sys
n = int(input())
x = [0]*n
for w in range(n):
    x[w] = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    for j in range(len(x[i])):
        if j == 0:  # 왼쪽의 i --> 왼쪽 값 쭉 더한 값 i +=i-1
            x[i][j] += x[i-1][j]
        elif j == len(x[i])-1:  # 오른쪽의 i --> 오른쪽 값 쭉 더한 값 i += i-1
            x[i][j] += x[i-1][j-1]
        elif j < len(x[i-1]):  # 그외 가운데
            x[i][j] += max(x[i-1][j], x[i-1][j-1])  # 이전 값 2개 중 큰 걸 기존값과 더해서 반환
print(max(x[n-1]))
