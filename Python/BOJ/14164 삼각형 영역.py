def check(a,b,c): # 삼각형 내부 점체크
    if c[1] <= a[1] or c[1] > b[1]: 
        return False
    return (b[1]-a[1])*c[0] < (b[1]-c[1])*a[0] + (c[1]-a[1])*b[0]

import sys
N = int(sys.stdin.readline())
tree = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)], key=lambda x:(x[1],-x[0])) # 내림차순
farm = [[0]*N for _ in range(N)] 
result = [0]*(N-2)

for i in range(N):
    for j in range(i+1,N):
        for k in range(N):
            if check(tree[i],tree[j],tree[k]): 
                farm[i][j] += 1 # 심기 가능

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if check(tree[i],tree[k],tree[j]):
                x = farm[i][k] - farm[i][j] - farm[j][k] -1 
                if check(tree[i],tree[j],tree[k]):
                    x += 1
                if check(tree[j],tree[k],tree[i]):
                    x += 1
            else :
                x = farm[i][j] + farm[j][k] - farm[i][k]
                if check(tree[i],tree[j],tree[k]):
                    x -= 1
                if check(tree[j],tree[k],tree[i]):
                    x -= 1
            result[x] += 1
for i in result:
    print(i)