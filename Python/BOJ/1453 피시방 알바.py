N = int(input())
sit = list(map(int, input().split()))
count = [0]*(101)
cnt = 0
for i in sit:
    if count[i] == 0:
        count[i] += 1
    else:
        cnt += 1
print(cnt)