n, d = map(int, input().split())
num = [str(i) for i in range(1,n+1)]
cnt = 0
for i in num:
    for j in list(i):
        if j == str(d):
            cnt +=1
print(cnt)