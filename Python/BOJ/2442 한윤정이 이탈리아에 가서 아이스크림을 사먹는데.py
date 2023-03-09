n, m = map(int, input().split()) 
ice = [[0]*n for _ in range(n)] # 아이스 조합
for i in range(m):
    i1, i2 = map(int, input().split())
    ice[i1 - 1][i2 - 1] = 1 #섞어 먹으면 안되는 조합
    ice[i2 - 1][i1 - 1] = 1 #섞어 먹으면 안되는 조합

result = 0
# 아이스크림을 3가지를 선택하는 경우의 수
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if ice[i][j] != 1 and ice[i][k] != 1 and ice[j][k] != 1: #섞어 먹을 수 있으면 
                result += 1

print(result)