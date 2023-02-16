a = []
for i in range(5):
    x = int(input())
    a.append(x)
a.sort()
print(sum(a)//5)
print(a[2])
