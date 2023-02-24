A, B = map(int, input().split())
temp = []
for i in range(1, B+1):
    for j in range(i):
        temp.append(i)
print(temp)
print(sum(temp[A-1:B]))