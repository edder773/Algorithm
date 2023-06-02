import sys
N = int(sys.stdin.readline())
num = [[0] * 10 for _ in range(N+1)]
for i in range(1, 10):
    num[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            num[i][j] = num[i-1][1]
        elif j == 9:
            num[i][j] = num[i-1][8]
        else : 
            num[i][j] = num[i-1][j-1] + num[i-1][j+1]
print(sum(num[N]) % 1000000000)