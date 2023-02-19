x = list(map(int, input().split()))
sums = 0
for i in x :
    sums += i*i
print(sums%10)