n = int(input())
x = list(map(int, input().split()))
if n == 1:
    print(x[0]*x[0])
else:
    print(max(x)*min(x))
