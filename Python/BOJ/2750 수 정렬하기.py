N = int(input())
a = []
for _ in range(N):
    X = int(input())
    a.append(X)
a.sort()
for i in range(N):
    print(a[i])
